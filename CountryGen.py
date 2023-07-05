import os
import shutil

countries = {
    "GER": {
        "name": "Germany",
        "def": "Germany",
        "adj": "German",
        "culture": "Western_European",
        "color": "79 114 43",
        "capital": 45,
        "ideology": "Pro_Soviet",
        "country_name": "democratic_republic",
        "party": "SED",
        "party_long": "Socialist Unity Party of Germany",
        "leader": "Erich Honecker",
        "subideology": "Marxism_Leninism",
        "title": "General_Secretary",
    },
    "FRA": {
        "name": "France",
        "def": "France",
        "adj": "French",
        "culture": "Western_European",
        "color": "44 63 204",
        "capital": 56,
        "ideology": "Non_Aligned",
        "country_name": "republic",
        "party": "PCF",
        "party_long": "French Communist Party",
        "leader": "Pierre Juquin",
        "subideology": "Communism",
        "title": "General_Secretary",
    }
}

for tag in countries:
    country = {
        "name": "Default Name",
        "def": "Default Name",
        "adj": "Default Adj",
        "culture": "Western_European",
        "color": "200 200 200",
        "capital": 1,
        "ideology": "Non_Aligned",
        "leader": "El Generico",
        "subideology": "Socialism",
        "title": "President",
    }
    for item in countries[tag]:
        country[item] = countries[tag][item]
    
    # common/country_tags/00_countries.txt
    country_tags = ""
    with open("common/country_tags/00_countries.txt", 'r') as file:
        country_tags = file.read()
    country_tags = country_tags.replace("# CountryGen-Entry", f'{tag} = "countries/{country["culture"]}.txt"\n# CountryGen-Entry')
    with open("common/country_tags/00_countries.txt", 'w') as file:
        file.write(country_tags)
    
    # common/countries/colors.txt
    colors = ""
    with open("common/countries/colors.txt", 'r') as file:
        colors = file.read()
    colors = colors.replace("# CountryGen-Entry", f'{tag} = {{\n\tcolor = rgb {{ {country["color"]} }}\n\tcolor_ui = rgb {{ {country["color"]} }}\n}}\n# CountryGen-Entry')
    with open("common/countries/colors.txt", 'w') as file:
        file.write(colors)

    # history/countries/<TAG> - <Name>.txt
    h_country_name = ""
    if "country_name" in country: h_country_name = f'\n\nset_variable = {{ country_name = token:dyn_{country["country_name"]} }}'
    if "leader_id" not in country:
        country["leader_id"] = f'{tag}_{country["leader"].replace(" ", "_")}'
    history = f'''capital = {country["capital"]}{h_country_name}
recruit_character = {country["leader_id"]}

set_popularities = {{
    {country["ideology"]} = 100
}}
set_politics = {{
    ruling_party = {country["ideology"]}
    last_election = "1990.1.1"
    election_frequency = 60
    elections_allowed = no
}}
set_variable = {{ subideology = token:SUBIDEOLOGY_{country["subideology"]} }}
set_variable = {{ title = token:TITLE_{country["title"]} }}

{country["leader_id"]} = {{
	set_variable = {{ Portrait_Code = 0 }}
	set_variable = {{ Portrait_Max = 0 }}
}}'''
    with open(f'history/countries/{tag} - {country["name"]}.txt', 'w') as file:
        file.write(history)
    
    # common/characters/<TAG>.txt
    characters = f'''characters = {{
    {country["leader_id"]} = {{
        name = {country["leader_id"]}
        portraits = {{
            civilian = {{
                large = "GFX_Portrait_{country["leader_id"]}_0"
            }}
        }}
        country_leader = {{
            ideology = {country["ideology"]}_type
            traits = {{ }}
            expire = "2020.1.1"
        }}
    }}
}}'''
    with open(f'common/characters/{tag}.txt', 'w') as file:
        file.write(characters)

    # localisation/english/country_<TAG>_l_english.yml
    party = ""
    if "party" in country: party = f'\n\n {tag}_{country["ideology"]}_party: "{country["party"]}"\n {tag}_{country["ideology"]}_party_long: "{country["party_long"]}"'
    localisation = f'''\ufeffl_english:
 {tag}: "{country["name"]}"
 {tag}_DEF: "{country["def"]}"
 {tag}_ADJ: "{country["adj"]}"{party}

 {country["leader_id"]}: "{country["leader"]}"'''
    with open(f"localisation/english/country_{tag}_l_english.yml", 'w', encoding="utf8") as file:
        file.write(localisation)

    # interface/Portraits.gfx
    portraits = ""
    with open("interface/Portraits.gfx", 'r') as file:
        portraits = file.read()
    portraits = portraits.replace("# CountryGen-Entry", f'spriteType = {{\n\t\tname = "GFX_Portrait_{country["leader_id"]}_0"\n\t\ttexturefile = "gfx/leaders/leader_unknown.dds"\n\t}}\n\t# CountryGen-Entry')
    with open("interface/Portraits.gfx", 'w') as file:
        file.write(portraits)

    # gfx/flags/<TAG>.tga
    if not os.path.exists(f'gfx/flags/{tag}.tga'):
        shutil.copyfile('gfx/flags/ZZZ.tga', f'gfx/flags/{tag}.tga')
        shutil.copyfile('gfx/flags/medium/ZZZ.tga', f'gfx/flags/medium/{tag}.tga')
        shutil.copyfile('gfx/flags/small/ZZZ.tga', f'gfx/flags/small/{tag}.tga')

    # NameGen.py
    nameGen = ""
    with open("NameGen.py", 'r') as file:
        nameGen = file.read()
    nameGen = nameGen.replace("# CountryGen-Entry", f'"{tag}": {{ "name": "{country["name"]}", "def": "{country["def"]}", "adj": "{country["adj"]}" }},\n\t# CountryGen-Entry')
    with open("NameGen.py", 'w') as file:
        file.write(nameGen)