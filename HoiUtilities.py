import os
def StateSetter(states, old, new):
    files = os.listdir('history/states')
    for filename in files:
        if "txt" in filename:
            filenamer = filename.replace(" ", "")
            fileId = int(filenamer[0:filenamer.index("-")])
            if fileId in states:
                print(filename)
                text = ""
                with open("history/states/"+filename, 'r', encoding='utf8') as file:
                    text = file.read()
                old_text = text
                text = text.replace(old, new)
                if text == old_text:
                    print("No change")
                else:
                    with open("history/states/"+filename, 'w', encoding='utf8') as file:
                        file.write(text)

                
