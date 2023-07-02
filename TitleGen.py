subideologies = [
    [ "Leader", "Leader" ]
]

# Scripted Loc
politics_scripted_localisation = ""
with open("common/scripted_localisation/politics_scripted_localisation.txt", 'r', encoding='utf8') as file:
    politics_scripted_localisation = file.read()

with open("common/scripted_localisation/politics_scripted_localisation.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_scripted_localisation = politics_scripted_localisation.replace("# Script-GetTitle", f"text = {{ trigger = {{ has_country_leader_with_trait = TITLE_{subideology[0]} }} localization_key = TITLE_{subideology[0]} }}\n\t# Script-GetTitle")
    file.write(politics_scripted_localisation)

# Traits
politics_traits = ""
with open("common/country_leader/politics_traits.txt", 'r', encoding='utf8') as file:
    politics_traits = file.read()

with open("common/country_leader/politics_traits.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_traits = politics_traits.replace("# Script-TitleTrait", f"TITLE_{subideology[0]} = {{}}\n\t# Script-TitleTrait")
    file.write(politics_traits)

# Effects
politics_scripted_effects = ""
with open("common/scripted_effects/politics_scripted_effects.txt", 'r', encoding='utf8') as file:
    politics_scripted_effects = file.read()

with open("common/scripted_effects/politics_scripted_effects.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_scripted_effects = politics_scripted_effects.replace("# Script-Remove_Title", f"if = {{ limit = {{ has_country_leader_with_trait = TITLE_{subideology[0]} }} remove_country_leader_trait = TITLE_{subideology[0]} }}\n\t# Script-Remove_Title")
    file.write(politics_scripted_effects)

# Triggers
politics_scripted_triggers = ""
with open("common/scripted_triggers/politics_scripted_triggers.txt", 'r', encoding='utf8') as file:
    politics_scripted_triggers = file.read()

with open("common/scripted_triggers/politics_scripted_triggers.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_scripted_triggers = politics_scripted_triggers.replace("# Script-Has_Title", f"has_country_leader_with_trait = TITLE_{subideology[0]}\n\t\t# Script-Has_Title")
    file.write(politics_scripted_triggers)

# Localisation
parties_l_english = ""
with open("localisation/english/parties_l_english.yml", 'r', encoding='utf8') as file:
    parties_l_english = file.read()

with open("localisation/english/parties_l_english.yml", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        parties_l_english = parties_l_english.replace("# Script-TitleLoc", f"TITLE_{subideology[0]}: \"{subideology[1]}\"\n # Script-TitleLoc")
    file.write(parties_l_english)
