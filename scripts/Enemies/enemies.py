import random
from Player_and_Classes.creation import user_data, types_of_classes
from Player_and_Classes.leveling import level_up
from Combat.moves_var import moves
from Combat.combat import deal_damage, damage_formula

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
    "name": enemy_name,
    "class": enemy_class,
    "level": enemy_level,
    "hp": random.randint(user_data["hp"] - 10, user_data["hp"] + 10),
    "stats": {
        "attack": 0,
        "speed": 0,
        "defense": 0
    }
}

for i in range(enemy["level"] - 1):
    level_up(True)
if enemy["class"] == "warrior":
    enemy["hp"] = example_stats["hp"] * 1.5
    enemy["stats"]["attack"] = example_stats["stats"]["attack"] * 1.5
    enemy["stats"]["defense"] = example_stats["stats"]["defense"] * 1
    enemy["stats"]["speed"] = example_stats["stats"]["speed"] * 1
    enemy["stats"]["mana"] = example_stats["stats"]["mana"] * 0
    enemy["stats"]["luck"] = example_stats["stats"]["luck"] * 1
    enemy["stats"]["crit_damage"] = example_stats["stats"]["crit_damage"] * 1
elif enemy["class"] == "mage":
    enemy["hp"] = example_stats["hp"] * 0.5
    enemy["stats"]["attack"] = example_stats["stats"]["attack"] * 0.5
    enemy["stats"]["defense"] = example_stats["stats"]["defense"] * 0.5
    enemy["stats"]["speed"] = example_stats["stats"]["speed"] * 1
    enemy["stats"]["mana"] = example_stats["stats"]["mana"] * 2.5
    enemy["stats"]["luck"] = example_stats["stats"]["luck"] * 1
    enemy["stats"]["crit_damage"] = example_stats["stats"]["crit_damage"] * 1
elif enemy["class"] == "archer":
    enemy["hp"] = example_stats["hp"] * 1
    enemy["stats"]["attack"] = example_stats["stats"]["attack"] * 1
    enemy["stats"]["defense"] = example_stats["stats"]["defense"] * 0.5
    enemy["stats"]["speed"] = example_stats["stats"]["speed"] * 1.5
    enemy["stats"]["mana"] = example_stats["stats"]["mana"] * 1
    enemy["stats"]["luck"] = example_stats["stats"]["luck"] * 2
    enemy["stats"]["crit_damage"] = example_stats["stats"]["crit_damage"] * 1
elif enemy["class"] == "tank":
    enemy["hp"] = example_stats["hp"] * 2
    enemy["stats"]["attack"] = example_stats["stats"]["attack"] * 0.5
    enemy["stats"]["defense"] = example_stats["stats"]["defense"] * 2
    enemy["stats"]["speed"] = example_stats["stats"]["speed"] * 0.5
    enemy["stats"]["mana"] = example_stats["stats"]["mana"] * 0
    enemy["stats"]["luck"] = example_stats["stats"]["luck"] * 0.5
    enemy["stats"]["crit_damage"] = example_stats["stats"]["crit_damage"] * 1
elif enemy["class"] == "shaman":
    enemy["hp"] = example_stats["hp"] * 1
    enemy["stats"]["attack"] = example_stats["stats"]["attack"] * 0.5
    enemy["stats"]["defense"] = example_stats["stats"]["defense"] * 1
    enemy["stats"]["speed"] = example_stats["stats"]["speed"] * 1
    enemy["stats"]["mana"] = example_stats["stats"]["mana"] * 2.5
    enemy["stats"]["luck"] = example_stats["stats"]["luck"] * 1.5
    enemy["stats"]["crit_damage"] = example_stats["stats"]["crit_damage"] * 1
elif enemy["class"] == "summoner":
    enemy["hp"] = example_stats["hp"] * 1
    enemy["stats"]["attack"] = example_stats["stats"]["attack"] * 0.5
    enemy["stats"]["defense"] = example_stats["stats"]["defense"] * 1
    enemy["stats"]["speed"] = example_stats["stats"]["speed"] * 0.5
    enemy["stats"]["mana"] = example_stats["stats"]["mana"] * 2.5
    enemy["stats"]["luck"] = example_stats["stats"]["luck"] * 1
    enemy["stats"]["crit_damage"] = example_stats["stats"]["crit_damage"] * 1
elif enemy["class"] == "wildcard":
    enemy["hp"] = example_stats["hp"] * 1
    enemy["stats"]["attack"] = example_stats["stats"]["attack"] * 1
    enemy["stats"]["defense"] = example_stats["stats"]["defense"] * 1
    enemy["stats"]["speed"] = example_stats["stats"]["speed"] * 1
    enemy["stats"]["mana"] = example_stats["stats"]["mana"] * 1
    enemy["stats"]["luck"] = example_stats["stats"]["luck"] * 1
    enemy["stats"]["crit_damage"] = example_stats["stats"]["crit_damage"] * 1


def enemy_turn():
    enemy_moves = [random.choice(
        [moves["General_Moves"], moves[enemy["class"]], moves[enemy["class"]]])]

    crit = True if random.randint(1, 100) < enemy["stats"]["luck"] else False

    deal_damage(enemy, damage_formula(
        enemy, user_data["stats"]["defense"], enemy["stats"]["attack"], ))
