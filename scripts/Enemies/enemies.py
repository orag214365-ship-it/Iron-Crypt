import random
from Player_and_Classes.creation import user_data, types_of_classes

types_of_enemys = ["Goblin", "Zombie", "Slime", "Skeleton"]

example_stats = {
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

enemy_name = random.choice(types_of_classes)
enemy_class = random.choice(types_of_classes)
enemy_level = random.choice([1 if user_data["level"] - 1 else user_data["level"] - 1, 1 if user_data["level"] -
                            2 else user_data["level"] - 2, user_data["level"] + 1, user_data["level"] + 2])


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
