import os
states = [ 329, 568, 576, 516, 878, 575, 567, 566, 564, 575, 565, 876, 574, 562, 877, 644, 822, 637, 562, 563, 561, 560, 657, 409, 408, 655, 537, 555, 763 ]
files = os.listdir('history/states')
new = "owner = SOV\n\t\tadd_core_of = SOV\n\t\tset_state_flag = country_russia"
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

            
