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

print(enemy_level)
