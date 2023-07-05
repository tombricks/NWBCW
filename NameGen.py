tags = {
    "CHI": { "name": "China", "def": "China", "adj": "Chinese" },
    "SOV": { "name": "Soviet Union", "def": "the Soviet Union", "adj": "Soviet" },
    "ALB": { "name": "Albania", "def": "Albania", "adj": "Albanian" },
    "GER": { "name": "Germany", "def": "Germany", "adj": "German" },
	"FRA": { "name": "France", "def": "France", "adj": "French" },
	# CountryGen-Entry
}
templates = {
    "peoples_republic_of": { "name": "People's Republic of $$NAME$$", "def": "the People's Republic of $$DEF$$" },
    "soviet_socialist_republic": { "name": "$$ADJ$$ Soviet Socialist Republic", "def": "the $$ADJ$$ Soviet Socialist Republic" },
    "democratic_republic": { "name": "$$ADJ$$ Democratic Republic", "def": "the $$ADJ$$ Democratic Republic" },
    "republic": { "name": "$$ADJ$$ Republic", "def": "the $$ADJ$$ Republic" },
    "peoples_socialist_republic_of": { "name": "People's Socialist Republic of $$DEF$$", "def": "the People's Socialist Republic of $$DEF$$" },
}
def setter(tag, template):
    return template.replace("$$NAME$$", tag["name"]).replace("$$DEF$$", tag["def"]).replace("$$ADJ$$", tag["adj"])

out = "\ufeffl_english:"
for template in templates:
    for tag in tags:
        out += "\n base_"+tag+"_dyn_"+template+": \""+setter(tags[tag], templates[template]["name"])+"\""
        out += "\n base_"+tag+"_dyn_"+template+"_DEF: \""+setter(tags[tag], templates[template]["def"])+"\""
    out += "\n dyn_"+template+": \""+setter({"name": "NAME", "def": "DEF", "adj": "ADJ"}, templates[template]["name"])+"\""
for tag in tags:
    out += "\n base_"+tag+": \""+tags[tag]["name"]+"\""
    out += "\n base_"+tag+"_DEF: \""+tags[tag]["def"]+"\""
    out += "\n base_"+tag+"_ADJ: \""+tags[tag]["adj"]+"\""

print(out)
with open("localisation/english/countries_generated_l_english.yml", 'w', encoding='utf8') as file:
    file.write(out)
with open("common/country_leader/country_name_traits.txt", 'w', encoding='utf8') as file:
    text = "leader_traits = {"
    for template in templates:
        text += "\n\tdyn_"+template+" = {}"
    for tag in tags:
        text += "\n\tbase_"+tag+" = {}"
    text += "\n}"
    file.write(text)
with open("history/general/country_names.txt", 'w', encoding='utf8') as file:
    text = ""
    for template in templates:
        text += f"add_to_array = {{ global.country_name_traits = token:dyn_{template} }}\n"
    file.write(text)