import json
import random
user_data_path = "user data/user_data.json"
base_stats = {
    "name": "",
    "class": "",
    "level": 1,
    "hp": 10,
    "stats": {
        "attack": 10,
        "defense": 3,
        "speed": 5
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
types_of_enemys = ["Goblin", "Zombie", "Slime", "Sceleton"]
types_of_classes = ["Warrior", "Mage", "Archer",
                    "Tank", "Shaman", "Summoner", "Wildcard"]
enemy_level = random.choice([user_data["level"] - 0 if user_data["level"] ==
                            1 else user_data["level"] - 1, user_data["level"] - 0 if user_data["level"] < 3 else user_data["level"] - 3, user_data["level"] + 1, user_data["level"] + 2])
moves = {
    "punch": {
        "description": "The most basic move does a bit of damage",
        "move_damage": 10
    },
    "kick": {
        "description": "Another very basic move does a bit of damage",
        "move_damage": 10
    }
}
user_moves = ["punch", "kick"]
invalid_command_prompt = "Please type a valid command. (Type ? for a list of commands"
enemy = {
    "name": random.choice(types_of_enemys),
    "class": random.choice(types_of_classes),
    "level": enemy_level,
    "hp": 50,
    "stats": {
        "attack": 10,
        "speed": 5,
        "defense": 3
    }
}
