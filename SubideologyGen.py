subideologies = [
    [ "Hoxhaism", "Hoxhaism", "Hoxhaist" ]
]

# Scripted Loc
politics_scripted_localisation = ""
with open("common/scripted_localisation/politics_scripted_localisation.txt", 'r', encoding='utf8') as file:
    politics_scripted_localisation = file.read()

with open("common/scripted_localisation/politics_scripted_localisation.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_scripted_localisation = politics_scripted_localisation.replace("# Script-GetSubideologyN", f"text = {{ trigger = {{ has_country_leader_with_trait = SUBIDEOLOGY_{subideology[0]} }} localization_key = SUBIDEOLOGY_{subideology[0]} }}\n\t# Script-GetSubideologyN")
        politics_scripted_localisation = politics_scripted_localisation.replace("# Script-GetSubideologyAdj", f"text = {{ trigger = {{ has_country_leader_with_trait = SUBIDEOLOGY_{subideology[0]} }} localization_key = SUBIDEOLOGY_{subideology[0]}_ADJ }}\n\t# Script-GetSubideologyAdj")
        politics_scripted_localisation = politics_scripted_localisation.replace("# Script-GetSubideologyDesc", f"text = {{ trigger = {{ has_country_leader_with_trait = SUBIDEOLOGY_{subideology[0]} }} localization_key = SUBIDEOLOGY_{subideology[0]}_desc }}\n\t# Script-GetSubideologyDesc")
        politics_scripted_localisation = politics_scripted_localisation.replace("# Script-GetSubideologyIcon", f"text = {{ trigger = {{ has_country_leader_with_trait = SUBIDEOLOGY_{subideology[0]} }} localization_key = GFX_SUBIDEOLOGY_{subideology[0]} }}\n\t# Script-GetSubideologyIcon")
    file.write(politics_scripted_localisation)

# Traits
politics_traits = ""
with open("common/country_leader/politics_traits.txt", 'r', encoding='utf8') as file:
    politics_traits = file.read()

with open("common/country_leader/politics_traits.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_traits = politics_traits.replace("# Script-SubideologyTrait", f"SUBIDEOLOGY_{subideology[0]} = {{}}\n\t# Script-SubideologyTrait")
    file.write(politics_traits)

# History
politics_history = ""
with open("history/general/politics.txt", 'r', encoding='utf8') as file:
    politics_history = file.read()

with open("history/general/politics.txt", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_history = politics_history.replace("# Script-SubideologyArray", f"add_to_array = {{ global.subideology_traits = token:TITLE_{subideology[0]} }}\n# Script-SubideologyArray")
    file.write(politics_history)

# Localisation
parties_l_english = ""
with open("localisation/english/parties_l_english.yml", 'r', encoding='utf8') as file:
    parties_l_english = file.read()

with open("localisation/english/parties_l_english.yml", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        parties_l_english = parties_l_english.replace("# Script-SubideologyLoc", f"SUBIDEOLOGY_{subideology[0]}: \"{subideology[1]}\"\n SUBIDEOLOGY_{subideology[0]}_ADJ: \"{subideology[2]}\"\n SUBIDEOLOGY_{subideology[0]}_desc: \"\"\n # Script-SubideologyLoc")
    file.write(parties_l_english)

# GFX
politics_gfx = ""
with open("interface/politics.gfx", 'r', encoding='utf8') as file:
    politics_gfx = file.read()

with open("interface/politics.gfx", 'w', encoding='utf8') as file:
    for subideology in subideologies:
        politics_gfx = politics_gfx.replace("# Script-SubideologyGFX", f"spriteType = {{\n\t\tname = \"GFX_SUBIDEOLOGY_{subideology[0]}\"\n\t\ttexturefile = \"gfx/interface/ideologies/SUBIDEOLOGY_{subideology[0]}.dds\"\n\t}}\n\t# Script-SubideologyGFX")
    file.write(politics_gfx)