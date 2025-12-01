from creation import user_data
from save_load import save_user_data
from Enemies.enemies import example_stats


def level_up(test):
    if test:
        example_stats["hp"] += 10
        example_stats["stats"]["attack"] += 1
        example_stats["stats"]["defense"] += 1
        example_stats["stats"]["speed"] += 1
        example_stats["stats"]["mana"] += 1
        example_stats["stats"]["luck"] += 0.05
    else:
        if user_data["class"] == "warrior":
            user_data["hp"] += 10
            user_data["stats"]["attack"] += 2
            user_data["stats"]["defense"] += 1
            user_data["stats"]["speed"] += 1
            user_data["stats"]["mana"] += 0
            user_data["stats"]["luck"] += 0
            user_data["stats"]["crit_damage"] += .05
            save_user_data()
        elif user_data["class"] == "mage":
            user_data["hp"] += 6
            user_data["stats"]["attack"] += 0
            user_data["stats"]["defense"] += 0
            user_data["stats"]["speed"] += 1
            user_data["stats"]["mana"] += 5
            user_data["stats"]["luck"] += 0
            user_data["stats"]["crit_damage"] += .05
            save_user_data()
        elif user_data["class"] == "archer":
            user_data["hp"] += 8
            user_data["stats"]["attack"] += 1
            user_data["stats"]["defense"] += 0
            user_data["stats"]["speed"] += 2
            user_data["stats"]["mana"] += .5
            user_data["stats"]["luck"] += .05
            user_data["stats"]["crit_damage"] += 0.05
            save_user_data()
        elif user_data["class"] == "tank":
            user_data["hp"] += 15
            user_data["stats"]["attack"] += 0
            user_data["stats"]["defense"] += 3
            user_data["stats"]["speed"] += 0
            user_data["stats"]["mana"] += 0
            user_data["stats"]["luck"] += .05
            user_data["stats"]["crit_damage"] += .05
            save_user_data()
        elif user_data["class"] == "shaman":
            user_data["hp"] += 5
            user_data["stats"]["attack"] += 1
            user_data["stats"]["defense"] += 0
            user_data["stats"]["speed"] += 1
            user_data["stats"]["mana"] += 5
            user_data["stats"]["luck"] += .05
            user_data["stats"]["crit_damage"] += .05
            save_user_data()
        elif user_data["class"] == "summoner":
            user_data["hp"] += 5
            user_data["stats"]["attack"] += 2
            user_data["stats"]["defense"] += 1
            user_data["stats"]["speed"] += 1
            user_data["stats"]["mana"] += 5
            user_data["stats"]["luck"] += .05
            user_data["stats"]["crit_damage"] += .05
            save_user_data()
        elif user_data["class"] == "wildcard":
            user_data["hp"] += 1
            user_data["stats"]["attack"] += 1
            user_data["stats"]["defense"] += 1
            user_data["stats"]["speed"] += 1
            user_data["stats"]["mana"] += 1
            user_data["stats"]["luck"] += 0.25
            user_data["stats"]["crit_damage"] += 0.05
            save_user_data()
