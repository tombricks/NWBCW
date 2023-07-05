subideologies = [
    [ "President", "President" ]
]

# Scripted Loc
politics_scripted_localisation = ""
with open("common/scripted_localisation/politics_scripted_localisation.txt", 'r', encoding='utf8') as file:
    politics_scripted_localisation = file.read()

with open("common/scripted_localisation/politics_scripted_localisation.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_scripted_localisation = politics_scripted_localisation.replace("# Script-GetTitle", f"text = {{ trigger = {{ check_variable = {{ title = token:TITLE_{subideology[0]} }} }} localization_key = TITLE_{subideology[0]} }}\n\t# Script-GetTitle")
    file.write(politics_scripted_localisation)

# Traits
politics_traits = ""
with open("common/country_leader/politics_traits.txt", 'r', encoding='utf8') as file:
    politics_traits = file.read()

with open("common/country_leader/politics_traits.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_traits = politics_traits.replace("# Script-TitleTrait", f"TITLE_{subideology[0]} = {{}}\n\t# Script-TitleTrait")
    file.write(politics_traits)

# History
politics_history = ""
with open("history/general/politics.txt", 'r', encoding='utf8') as file:
    politics_history = file.read()

with open("history/general/politics.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_history = politics_history.replace("# Script-TitleArray", f"add_to_array = {{ global.title_traits = token:TITLE_{subideology[0]} }}\n# Script-TitleTrait")
    file.write(politics_history)

# Localisation
parties_l_english = ""
with open("localisation/english/parties_l_english.yml", 'r', encoding='utf8') as file:
    parties_l_english = file.read()

with open("localisation/english/parties_l_english.yml", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        parties_l_english = parties_l_english.replace("# Script-TitleLoc", f"TITLE_{subideology[0]}: \"{subideology[1]}\"\n # Script-TitleLoc")
    file.write(parties_l_english)
