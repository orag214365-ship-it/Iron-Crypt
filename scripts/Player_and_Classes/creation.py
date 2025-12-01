import json
from save_load import save_user_data

class_descriptions = {
    "Warrior": "The master of phisical combat. An all rounder that can do everything exept magic.",
    "Mage": "A scholer from the University of Arcane Arts. Amazing damage but not so amazing health.",
    "Archer": "Master of the bow and crosbow. Other than high acurracy and high crit rate has basic stats.",
    "Tank": "A Warrior that lost his familly and swore to protect everyone. Very very high defense low on everything else.",
    "Shaman": "An outsider from the University of Arcane Arts. Like the mage but Heals and Debufs instead.",
    "Summoner": "A prizzinor banised from the University of Arcane Arts because of dark magic. Summons creatures to fight.",
    "WildCard": '"Dad told me to stop... i never did". A gambler from a faraway town can either do alot of damage or very little.'
}

user_data_path = "user data/user_data.json"

types_of_classes = ["warrior", "mage", "archer",
                    "tank", "shaman", "summoner", "wildcard"]

base_stats = {
    "name": "",
    "class": "",
    "level": 1,
    "hp": 120,
    "donewithcreation": 0,
    "stats": {
        "attack": 15,
        "defense": 12,
        "speed": 10,
        "crit_damage": 2,
        "luck": 5,
        "mana": 10
    }
}

try:
    with open(user_data_path, "r") as f:
        user_data = json.load(f)
except FileNotFoundError:
    with open(user_data_path, "w") as f:
        json.dump(base_stats, f, indent=4)
    with open(user_data_path, "r") as f:
        user_data = json.load(f)


def set_stats_for_class(clas):
    if clas == "warrior":
        user_data["hp"] = 180
        user_data["stats"]["attack"] = 22
        user_data["stats"]["defense"] = 12
        user_data["stats"]["speed"] = 10
        user_data["stats"]["mana"] = 0
        user_data["stats"]["luck"] = 10
        user_data["stats"]["crit_damage"] = 2
        save_user_data()
    elif clas == "mage":
        user_data["hp"] = 60
        user_data["stats"]["attack"] = 7
        user_data["stats"]["defense"] = 6
        user_data["stats"]["speed"] = 10
        user_data["stats"]["mana"] = 40
        user_data["stats"]["luck"] = 15
        user_data["stats"]["crit_damage"] = 2
        save_user_data()
    elif clas == "archer":
        user_data["hp"] = 120
        user_data["stats"]["attack"] = 15
        user_data["stats"]["defense"] = 6
        user_data["stats"]["speed"] = 15
        user_data["stats"]["mana"] = 10
        user_data["stats"]["luck"] = 20
        user_data["stats"]["crit_damage"] = 2.5
        save_user_data()
    elif clas == "tank":
        user_data["hp"] = 240
        user_data["stats"]["attack"] = 7
        user_data["stats"]["defense"] = 24
        user_data["stats"]["speed"] = 5
        user_data["stats"]["mana"] = 0
        user_data["stats"]["luck"] = 5
        user_data["stats"]["crit_damage"] = 2
        save_user_data()
    elif clas == "shaman":
        user_data["hp"] = 120
        user_data["stats"]["attack"] = 7
        user_data["stats"]["defense"] = 12
        user_data["stats"]["speed"] = 10
        user_data["stats"]["mana"] = 40
        user_data["stats"]["luck"] = 17
        user_data["stats"]["crit_damage"] = 2
        save_user_data()
    elif clas == "summoner":
        user_data["hp"] = 120
        user_data["stats"]["attack"] = 7
        user_data["stats"]["defense"] = 12
        user_data["stats"]["speed"] = 5
        user_data["stats"]["mana"] = 40
        user_data["stats"]["luck"] = 10
        user_data["stats"]["crit_damage"] = 2
        save_user_data()
    elif clas == "shaman":
        user_data["hp"] = 120
        user_data["stats"]["attack"] = 15
        user_data["stats"]["defense"] = 12
        user_data["stats"]["speed"] = 10
        user_data["stats"]["mana"] = 10
        user_data["stats"]["luck"] = 15
        user_data["stats"]["crit_damage"] = 2
        save_user_data()


def create_player():
    while True:
        user_data["name"] = input("What is your name? >> ")
        while True:
            class_select_input = input(
                "What class do you want? (Type ? for a list of classes) >> ").lower()

            if class_select_input in ["help", "?"]:
                for k, v in class_descriptions.items():
                    print(f"{k}: {v}")
                    if k == "WildCard":
                        break
            elif class_select_input in types_of_classes:
                user_data["class"] = class_select_input
                break

        if input(f'Is this correct? (anything other than "yes" will be counted as no\n name: {user_data["name"]}\n class: {user_data["class"]}\n >> ').lower() == "yes":
            user_data["donewithcreation"] = 1
            save_user_data()
            break
        else:
            continue
