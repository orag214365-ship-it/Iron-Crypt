import random
from Player_and_Classes.creation import user_data, types_of_classes

types_of_enemys = ["Goblin", "Zombie", "Slime", "Skeleton"]

enemy_level = random.choice([user_data["level"] - 0 if user_data["level"] ==
                            1 else user_data["level"] - 1, user_data["level"] - 0 if user_data["level"] < 3 else user_data["level"] - 3, user_data["level"] + 1, user_data["level"] + 2])
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
