countries = {
    "GER": {
        "name": "Germany",
        "def": "Germany",
        "adj": "German",
        "culture": "Western_European",
        "color": "79 114 43"
        "capital": 45,
        "ideology": "Pro_Soviet",
        "party": "SED",
        "party_long": "Socialist Unity Party of Germany",
        "leader": "Erich Honecker",
        "subideology": "Marxism_Leninism",
        "title": "General_Secretary",
    }
}

for tag in countries:
    country = {
        "name": "Default Name",
        "def": "Default Name",
        "adj": "Default Adj",
        "culture": "Western_European",
        "color": "200 200 200"
        "capital": 1,
        "ideology": "Non_Aligned",
        "leader": "Erich Honecker",
        "subideology": "Socialism",
        "title": "President",
    }
    for item in countries[tag]:
        country[item] = countries[tag][item]
    
    # common/country_tags/00_countries.txt
    country_tags = ""
    with open("common/country_tags/00_countries.txt", 'r') as file:
        country_tags = file.read()
    country_tags = country_tags.replace("# CountryGen-Entry")
    # common/countries/colors.txt
    # history/countries/<TAG> - <Name>.txt
    # gfx/flags/<TAG>.tga
    # localisation/english/country_<TAG>_l_english.yml
    # NameGen.py