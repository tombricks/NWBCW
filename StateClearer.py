import os
stateNames = {}
with open("localisation/english/state_names_l_english.yml", 'r', encoding='utf8') as file:
    x = -1
    for line in file.readlines():
        x += 1
        if (x >= 1):
            nl = line.strip()
            name = nl[nl.index('"')+1:-1]
            sid = nl[0:nl.index(':')].replace("STATE_", "")
            if sid.isnumeric():
                stateNames[int(sid)] = name
            else:
                print(sid)

stateProvs = {}
for filename in os.listdir('history/states/in/'):
    if 'txt' not in filename:
        continue
    y = int(filename[0:filename.index("-")].strip())
    stateProvs[y] = []
    stateText = ""
    with open("history/states/in/"+filename, 'r', encoding='utf8') as file:
        for line in file.readlines():
            if "#" in line:
                line = line[0:line.index("#")]
            stateText += line.replace("\n", "") + "\n"
    stateThings = stateText.replace('=', ' = ').replace('{', ' { ').replace('}', ' } ').replace('\n', ' ').split(' ')
    prov = False
    x = -1
    for thing in stateThings:
        x += 1
        if thing.strip() != "":
            thing = thing.strip()
            if thing == "provinces":
                prov = True
            elif prov:
                if thing.isnumeric():
                    stateProvs[y].append(thing)
                elif thing == "}":
                    prov = False

for stateID in range(1, 909):
    stateFile = f"""state = {{
\tid = {stateID}
\tname = "STATE_{stateID}" # {stateNames[stateID]}
\tmanpower = 1
\tstate_category = wasteland
\t
\thistory = {{
\t\towner = ZZZ
\t}}
\t
\tprovinces = {{
\t\t{" ".join(stateProvs[stateID])}
\t}}
\t
\tlocal_supplies = 10
}}"""
    with open('history/states/out/'+str(stateID)+' - '+stateNames[stateID]+".txt", 'w', encoding='utf8') as file:
        file.write(stateFile)
