import json
import random

def load_data(file_name):
    with open('data/' + file_name + '.json', 'r') as f:
        data = json.load(f)

    if file_name == 'profession_skills':
        data = {item['Profession']: item['Skills'] for item in data}
    elif file_name == 'physical_attributes':
        data = {item['Race']: item for item in data}
    elif file_name == 'profession_backstories':
        data = {item['Profession']: item['Backstories'] for item in data}
    return data



races = load_data('races')
alignments = load_data('alignments')
skills = load_data('skills')
first_names = load_data('first_names')
last_names = load_data('last_names')
professions = load_data('professions')
profession_backstories = load_data('profession_backstories') 
generic_backstories = load_data('generic_backstories')
physical_attributes = load_data('physical_attributes')


#profession based functions
profession_skills = load_data('profession_skills')
weapons = load_data('weapons')
armor = load_data('armor')
clothing = load_data('clothing')
tools = load_data('tools')
misc_items = load_data('misc_items')




def generate_name():
    return random.choice(first_names) + ' ' + random.choice(last_names)





def generate_npc():

    race = random.choice(races)
    profession = random.choice(professions)
    name = generate_name()
    backstory, physical_features, quirks = generate_backstory(profession)


    # Change number or change code to "random.sample(clothing[profession], 2) if len(clothing[profession]) >= 2 else clothing[profession]" 
    # if you want more or less items from each category
    chosen_weapon = random.choice(weapons[profession]) if weapons[profession] else None
    chosen_armor = random.choice(armor[profession]) if armor[profession] else None
    chosen_clothing = random.sample(clothing[profession], 2) if len(clothing[profession]) >= 2 else clothing[profession]
    chosen_tool = random.choice(tools[profession]) if tools[profession] else None
    chosen_misc_item = random.choice(misc_items[profession]) if misc_items[profession] else None

    attributes = {
        'Strength': random.randint(1, 20),
        'Dexterity': random.randint(1, 20),
        'Constitution': random.randint(1, 20),
        'Intelligence': random.randint(1, 20),
        'Wisdom': random.randint(1, 20),
        'Charisma': random.randint(1, 20)
    }
    alignment = random.choice(alignments)
    npc_skills = profession_skills[profession]

    # Get physical attributes data for the chosen race
    race_attributes = physical_attributes[race]

    # Randomly choose physical attributes
    height_category = random.choice(race_attributes['Height'])
    height = round(random.uniform(height_category['MinHeight'], height_category['MaxHeight']), 1)
    weight = random.choice(race_attributes['Weight'])
    hair_color = random.choice(race_attributes['HairColor'])
    eye_color = random.choice(race_attributes['EyeColor'])
    skin_color = random.choice(race_attributes['SkinColor'])

    return {
        'Name': name,
        'Race': race,
        'Profession': profession,
        'Attributes': attributes,
        'Alignment': alignment,
        'Skills': npc_skills,
        'Backstory' : backstory,
        'Physical Features': physical_features,
        'Quirks': quirks,
        'Physical Description': {
            'Height': f'{height} ft ({height_category["Type"]})',
            'Weight': weight,
            'Hair Color': hair_color,
            'Eye Color': eye_color,
            'Skin Color': skin_color,
        },
        'Equipment': {
            'Weapons': chosen_weapon,
            'Armor': chosen_armor,
            'Clothing': chosen_clothing,
            'Tools': chosen_tool,
            'Misc_Items': chosen_misc_item
        }
    }

def generate_backstory(profession):
    if random.random() < 0.5:
        backstory_entry = random.choice(profession_backstories[profession])
        backstory = backstory_entry['Story']
        physical_features = random.choice(backstory_entry['PhysicalFeatures'])
        quirks = random.choice(backstory_entry['Quirks'])
    else:
        backstory_entry = random.choice(generic_backstories)
        backstory = backstory_entry['Backstory']
        physical_features = random.choice(backstory_entry['PhysicalFeatures'])
        quirks = random.choice(backstory_entry['Quirks'])
    return backstory, [physical_features], [quirks]






def display_npc(npc):
    print("Name:", npc['Name'])
    print("Race:", npc['Race'])
    print("Profession:", npc['Profession'])
    print("Attributes:")
    for attr, value in npc['Attributes'].items():
        print(f"  {attr}: {value}")
    print("Alignment:", npc['Alignment'])
    print("Skills:", ', '.join(npc['Skills']))
    print("Backstory:", npc['Backstory'])
    print("Physical Description:")
    for attr, value in npc['Physical Description'].items():
        print(f"  {attr}: {value}")
    print("Physical Features:", ', '.join(npc['Physical Features']))
    print("Quirks:", ', '.join(npc['Quirks']))
    print("Equipment:")
    for item, value in npc['Equipment'].items():
        print(f"  {item}: {value}")





if __name__ == "__main__":
    npc = generate_npc()
    display_npc(npc)
