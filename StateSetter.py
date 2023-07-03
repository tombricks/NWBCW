import os
states = [ 620, 592, 729  ]
files = os.listdir('history/states')
new = "owner = CHI\n\t\tadd_core_of = CHI"
for filename in files:
    if "txt" in filename:
        fileId = int(filename[0:filename.index(" ")])
        if fileId in states:
            print(filename)
            text = ""
            with open("history/states/"+filename, 'r', encoding='utf8') as file:
                text = file.read()
            old_text = text
            text = text.replace('owner = ZZZ', new)
            if text == old_text:
                print("No change")
            else:
                with open("history/states/"+filename, 'w', encoding='utf8') as file:
                    file.write(text)

            
