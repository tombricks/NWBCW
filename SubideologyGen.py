subideologies = [
    [ "Socialism", "Socialism", "Socialist" ]
]

# Scripted Loc
politics_scripted_localisation = ""
with open("common/scripted_localisation/politics_scripted_localisation.txt", 'r', encoding='utf8') as file:
    politics_scripted_localisation = file.read()

with open("common/scripted_localisation/politics_scripted_localisation.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_scripted_localisation.replace("# Script-GetSubideologyN", f"text = {{ trigger = {{ has_country_leader_with_trait = SUBIDEOLOGY_{subideology[0]} }} localization_key = SUBIDEOLOGY_{subideology[0]} }}\n\t# Script-GetSubideologyN")
        politics_scripted_localisation.replace("# Script-GetSubideologyAdj", f"text = {{ trigger = {{ has_country_leader_with_trait = SUBIDEOLOGY_{subideology[0]} }} localization_key = SUBIDEOLOGY_{subideology[0]}_ADJ }}\n\t# Script-GetSubideologyAdj")
        politics_scripted_localisation.replace("# Script-GetSubideologyIcon", f"text = {{ trigger = {{ has_country_leader_with_trait = SUBIDEOLOGY_{subideology[0]} }} localization_key = GFX_SUBIDEOLOGY_{subideology[0]} }}\n\t# Script-GetSubideologyIcon")
    file.write(politics_scripted_localisation)

# Traits
politics_traits = ""
with open("common/country_leader/politics_traits.txt", 'r', encoding='utf8') as file:
    politics_traits = file.read()

with open("common/country_leader/politics_traits.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_traits.replace("# Script-SubideologyTrait", f"SUBIDEOLOGY_{subideology[0]} = {{}}\n\t# Script-SubideologyTrait")

# Effects
politics_scripted_effects = ""
with open("common/scripted_effects/politics_scripted_effects.txt", 'r', encoding='utf8') as file:
    politics_scripted_effects = file.read()

with open("common/scripted_effects/politics_scripted_effects.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_scripted_effects.replace("# Script-Remove_Subideology", f"if = {{ limit = {{ has_country_leader_with_trait = SUBIDEOLOGY_{subideology[0]} }} remove_country_leader_trait = SUBIDEOLOGY_{subideology[0]} }}\n\t# Script-Remove_Subideology")

# Triggers
politics_scripted_triggers = ""
with open("common/scripted_triggers/politics_scripted_triggers.txt", 'r', encoding='utf8') as file:
    politics_scripted_triggers = file.read()

with open("common/scripted_triggers/politics_scripted_triggers.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_scripted_triggers.replace("# Script-Has_Subideology", f"has_country_leader_with_trait = SUBIDEOLOGY_{subideology[0]}\n\t\t# Script-Has_Subideology")

# Localisation
parties_l_english = ""
with open("localisation/english/parties_l_english.yml", 'r', encoding='utf8') as file:
    parties_l_english = file.read()

with open("localisation/english/parties_l_english.yml", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        parties_l_english.replace("# Script-SubideologyLoc", f"SUBIDEOLOGY_{subideology[0]}: \"{subideology[1]}\"\n SUBIDEOLOGY_{subideology[0]}_ADJ: \"{subideology[2]}\"\n # Script-SubideologyLoc")