from other import deal_damage, damage_formula
from variables import enemy, user_data, moves
from inputs import base_combat_input, attack_combat_input
import random


def player_turn():
    while True:
        combat_user_input = base_combat_input()

        if combat_user_input == "attack":
            if attack_combat_input() == "attacked":
                break
        elif combat_user_input == "ran away":
            break


def enemy_turn():
    move_list = list(moves.keys())
    enemy_moves = [random.choice(move_list), random.choice(move_list)]
    enemy_attack = random.choice(enemy_moves)
    deal_damage(user_data, damage_formula(
        'player', user_data["stats"]["defense"], enemy["stats"]["attack"], moves[enemy_attack]["move_damage"]))
    print(
        f"Enemy used {enemy_attack} you now have {user_data["hp"] if user_data["hp"] > 0 else 0} hp")
    if user_data["hp"] > 1:
        print("It is now your turn")
        return True
    else:
        print(f"The {enemy["name"]} killed you")
        return False


def combat():
    print(f"You found a {enemy['name']}")
    if enemy["stats"]["speed"] > user_data["stats"]["speed"]:
        while True:
            if not enemy_turn():
                break
            player_turn()
    else:
        while True:
            player_turn()
            if not enemy_turn():
                break


combat()
