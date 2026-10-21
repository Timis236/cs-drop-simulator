import os
import random

skin_dict = {}
with open("skin_ids.txt", encoding="utf8") as f:
    for line in f:
        (key, val) = line.strip("\n").split(";")
        if (not key.lower() in skin_dict):
            skin_dict[key.lower()] = val
        
weapon_dict = {}
with open("weapon_ids.txt", encoding="utf8") as f:
    for line in f:
        (key, val) = line.strip("\n").split(";")
        weapon_dict[key.lower()] = val

consumer_prefix = "\033[38;5;231m"
industrial_prefix = "\033[38;5;45m"
milspec_prefix = "\033[38;5;21m"
restricted_prefix = "\033[38;5;93m"
classified_prefix = "\033[38;5;201m"
covert_prefix = "\033[38;5;196m"
gold_prefix = "\033[38;5;220m"
suffix = "\033[0m"

collection_mode = False

# Get desired collection
files = os.listdir("collections/")
collections = []
for i in files:
    collections.append(i[:-4].replace("_", " "))

collection = ""
while (not collection.lower() in collections):
    collection = input("What collection/case would you like to recieve from? (\"list\" for available collections/cases): ")
    if (collection.lower() == "list"):
        for i in collections:
            print("    " + i)
            
# Initialize
collection = collection.lower()
if (collection.endswith("collection")):
    collection_mode = True

file = open("collections/" + collection.replace(" ", "_") + ".txt", "r")
collection_text = file.readlines()
file.close()

consumer = []
industrial = []
milspec = []
restricted = []
classified = []
covert = []
gold = []

current_grade = ""
for i in range(len(collection_text)):
    if (len(collection_text[i][:-1].split()) == 2):
        line = collection_text[i][:-1].split()
        if (current_grade == "consumer"):
            consumer.append([line[0].replace("_", " ").replace("|", " | "), [float(line[1][1:-1].split("-")[0]), float(line[1][1:-1].split("-")[1])]])
        if (current_grade == "industrial"):
            industrial.append([line[0].replace("_", " ").replace("|", " | "), [float(line[1][1:-1].split("-")[0]), float(line[1][1:-1].split("-")[1])]])
        if (current_grade == "mil-spec"):
            milspec.append([line[0].replace("_", " ").replace("|", " | "), [float(line[1][1:-1].split("-")[0]), float(line[1][1:-1].split("-")[1])]])
        if (current_grade == "restricted"):
            restricted.append([line[0].replace("_", " ").replace("|", " | "), [float(line[1][1:-1].split("-")[0]), float(line[1][1:-1].split("-")[1])]])
        if (current_grade == "classified"):
            classified.append([line[0].replace("_", " ").replace("|", " | "), [float(line[1][1:-1].split("-")[0]), float(line[1][1:-1].split("-")[1])]])
        if (current_grade == "covert"):
            covert.append([line[0].replace("_", " ").replace("|", " | "), [float(line[1][1:-1].split("-")[0]), float(line[1][1:-1].split("-")[1])]])
    
    if (len(collection_text[i][:-1].split()) == 1):
        current_grade = collection_text[i][:-1].lower()
        if (current_grade == "gold"):
            knife_collection = collection_text[i + 1][:-1].lower()
            
            file = open("knives/" + knife_collection + ".txt")
            knife_text = file.readlines()
            file.close
            
            finishes = knife_text[0][:-1].lower().replace(" ", "_")
            file = open("knives/finishes/" + finishes + ".txt")
            finish_text = file.readlines()
            file.close
            
            for j in range(1, len(knife_text)):
                knife = knife_text[j][:-1].replace("_", " ")
                for k in range(len(finish_text)):
                    line = finish_text[k][:-1].split()
                    gold.append([knife + " | " + line[0].replace("_", " "), [float(line[1][1:-1].split("-")[0]), float(line[1][1:-1].split("-")[1])]])
            
            i = i + 1
                
#print(consumer)
#print(industrial)
#print(milspec)
#print(restricted)
#print(classified)
#print(covert)
#print(gold)
print()

# Main loop
print("Contains one of the following:")
for i in consumer:
    print(consumer_prefix + i[0] + suffix)
for i in industrial:
    print(industrial_prefix + i[0] + suffix)
for i in milspec:
    print(milspec_prefix + i[0] + suffix)
for i in restricted:
    print(restricted_prefix + i[0] + suffix)
for i in classified:
    print(classified_prefix + i[0] + suffix)
for i in covert:
    print(covert_prefix + i[0] + suffix)
if (len(gold) > 0):
    print(gold_prefix + "or an Exceedingly Rare Special Item!" + suffix)

print()

print("Press ENTER to recieve a drop, and type \"exit\" to end the simulation.")
open_str = input()
while (open_str.lower() != "exit"):
    # Get skin name and float limits
    skin = None
    weapon_grade = None
    
    if (len(consumer) == 0 or (random.randint(1, 100) > 80 and len(industrial) > 0)):
        if (len(industrial) == 0 or (random.randint(1, 100) > 80 and len(milspec) > 0)):
            if (len(milspec) == 0 or (random.randint(1, 100) > 80 and len(restricted) > 0)):
                if (len(restricted) == 0 or (random.randint(1, 100) > 80 and len(classified) > 0)):
                    if (len(classified) == 0 or (random.randint(1, 100) > 80 and len(covert) > 0)):
                        if (len(covert) == 0 or (random.randint(1, 100) > 80 and len(gold) > 0)):
                            index = random.randint(0, len(gold) - 1)
                            skin = gold[index]
                            weapon_grade = "gold"
                        else:
                            index = random.randint(0, len(covert) - 1)
                            skin = covert[index]
                            weapon_grade = "covert"
                    else:
                        index = random.randint(0, len(classified) - 1)
                        skin = classified[index]
                        weapon_grade = "classified"
                else:
                    index = random.randint(0, len(restricted) - 1)
                    skin = restricted[index]
                    weapon_grade = "restricted"
            else:
                index = random.randint(0, len(milspec) - 1)
                skin = milspec[index]
                weapon_grade = "milspec"
        else:
            index = random.randint(0, len(industrial) - 1)
            skin = industrial[index]
            weapon_grade = "industrial"
    else:
        index = random.randint(0, len(consumer) - 1)
        skin = consumer[index]
        weapon_grade = "consumer"
        
    # Determine doppler type if necessary
    if (skin[0].endswith("Gamma_Doppler")):
        if (random.randint(1, 1000) > 916):
            skin[0] = skin[0] + " (Emerald)"
        else:
            skin[0] = skin[0] + " (Phase " + str(random.randint(1, 4)) + ")"
    #elif (skin[0].endswith("Doppler")):
        
    
    # Get float and wear rating
    float_value = None
    wear_rating = None
    
    roll = random.randint(1, 100)
    if (roll >= 1 and roll <= 3):
        float_value = random.uniform(0, 0.07)
    if (roll >= 4 and roll <= 27):
        float_value = random.uniform(0.07, 0.15)
    if (roll >= 28 and roll <= 60):
        float_value = random.uniform(0.15, 0.38)
    if (roll >= 61 and roll <= 84):
        float_value = random.uniform(0.38, 0.45)
    if (roll >= 85 and roll <= 100):
        float_value = random.uniform(0.45, 1)
    
    float_value = float_value * (skin[1][1] - skin[1][0]) + skin[1][0]
    if (float_value > 0 and float_value < 0.07):
        wear_rating = "Factory New"
    if (float_value > 0.07 and float_value < 0.15):
        wear_rating = "Minimal Wear"
    if (float_value > 0.15 and float_value < 0.38):
        wear_rating = "Field-Tested"
    if (float_value > 0.38 and float_value < 0.45):
        wear_rating = "Well-Worn"
    if (float_value > 0.45 and float_value < 1):
        wear_rating = "Battle-Scarred"
        
    # Get paint seed
    paint_seed = random.randint(0, 999)
    
    # Determine StatTrak
    stattrak = ""
    if (collection_mode == False and random.randint(1, 100) > 90):
        stattrak = "StatTrak™ "
    
    # Construct final output
    skin_output = ""
    
    if (weapon_grade == "consumer"):
        skin_output = skin_output + consumer_prefix
    if (weapon_grade == "industrial"):
        skin_output = skin_output + industrial_prefix
    if (weapon_grade == "milspec"):
        skin_output = skin_output + milspec_prefix
    if (weapon_grade == "restricted"):
        skin_output = skin_output + restricted_prefix
    if (weapon_grade == "classified"):
        skin_output = skin_output + classified_prefix
    if (weapon_grade == "covert"):
        skin_output = skin_output + covert_prefix
    if (weapon_grade == "gold"):
        skin_output = skin_output + gold_prefix + "★ "
    
    skin_output = skin_output + stattrak + skin[0] + " (" + wear_rating + ")" + suffix
    
    # Generate Weapon/Skin ID
    #weapon_name = 
    #weapon_id = weapon_dict[weapon_name.lower()]

    #skin_name = 
    #skin_id = skin_dict[paint_name.lower()]
    
    print("You opened:")
    print()
    print(skin_output)
    print()
    print("Float: " + str(float_value))
    print("Paint Seed: " + str(paint_seed))
    print()
    #print("Gen Code (copied to clipboard): !g " + weapon_id + " " + skin_id + " " + str(paint_seed) + " " + str(float_value))
    #print()
    open_str = input()
    