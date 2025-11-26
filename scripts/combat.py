import random
from variables import types_of_enemys, types_of_classes


def encounter_enemy():
    enemy = {
        "name": random.choice(types_of_enemys),
        "class": random.choice(types_of_classes),
        "level": 1,
        "hp": 50,
        "stats": {
            "attack": 10,
            "speed": 5,
            "defense": 3
        }
    }
    while True:
