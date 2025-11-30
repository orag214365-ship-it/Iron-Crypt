import json
import random
user_data_path = "user data/user_data.json"
base_stats = {
    "name": "",
    "class": "",
    "level": 1,
    "hp": 120,
    "stats": {
        "attack": 15,
        "defense": 12,
        "speed": 10
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
types_of_enemys = ["Goblin", "Zombie", "Slime", "Skeleton"]
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
    },
    "bite": {
        "description": "You lunge forward biting your enemy",
        "move_damage": 10
    },
    "arrow": {
        "description": "You use a bow and arrow to attack",
        "move_damage": 1
    }
}
user_moves = ["punch", "kick"]
invalid_command_prompt = "Please type a valid command. (Type ? for a list of commands"
enemy_attack = random.randint(
    user_data["stats"]["attack"] - 5, user_data["stats"]["attack"] + 5)
enemy_defense = random.randint(
    user_data["stats"]["defense"] - 5, user_data["stats"]["defense"] + 5)
enemy_speed = random.randint(
    user_data["stats"]["speed"] - 5, user_data["stats"]["speed"] + 5)
enemy = {
    "name": random.choice(types_of_enemys),
    "class": random.choice(types_of_classes),
    "level": enemy_level,
    "hp": random.randint(user_data["hp"] - 10, user_data["hp"] + 10),
    "stats": {
        "attack": enemy_attack,
        "speed": enemy_speed,
        "defense": enemy_defense
    }
}
base_commands = ["close", "cl", "?", "help", "h", "clear", "c"]
base_command_description = '"Close, cl": closes the game\n' \
    '"?, help, h": shows this list\n' \
    '"attack, a": do an attack\n' \
    '"clear, c": clears the terminal'
