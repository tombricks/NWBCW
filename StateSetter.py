import os
states = [ 558, 813, 1015, 558, 567, 564, 562, 572, 570, 559, 1072, 582, 583, 586, 560, 578, 585, 588, 589, 592, 591 ]
files = os.listdir('history/states')
new = "owner = CHI\n\t\tadd_core_of = CHI"
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
            text = text.replace('owner = ZZZ', new)
            if text == old_text:
                print("No change")
            else:
                with open("history/states/"+filename, 'w', encoding='utf8') as file:
                    file.write(text)

            
