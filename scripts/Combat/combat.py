import random
from Player_and_Classes.creation import user_data
from General_Helpers.general_var import base_commands, invalid_command_prompt, base_command_description, user_moves
from General_Helpers.general import close_confirmation, clear_terminal
from Enemies.enemies import enemy
from moves_var import moves


def move_info():
    pass


def deal_damage(target, amount):
    if target == 'player':
        target == user_data
    target["hp"] -= amount


def damage_formula(target, defense, attack_damage, movedamage):
    crit_chance = random.randint(0, 100)
    if crit_chance < 5:
        print(f"A citical hit!")
    if target == 'player':
        return 1 if round((movedamage + attack_damage ** 1.3) * (1 if crit_chance > 5 else 2) - (defense ** 0.9)) < 1 else round((movedamage + attack_damage ** 1.3) * (1 if crit_chance > 5 else 2) - (defense ** 0.9) * random.uniform(1.1, 1.5))
    else:
        return 1 if round(((movedamage + attack_damage ** 1.3) * (1 if crit_chance > 5 else 2) - (defense ** 0.9)) / 1.5) < 1 else round(((movedamage + attack_damage ** 1.3) * (1 if crit_chance > 5 else 2) - (defense ** 0.9)) / 1.5 * random.uniform(1.1, 1.5))


def base_combat_input():
    while True:
        user_input = input(
            "What do you want to do? (Type ? for a list of commands) >> ").lower()
        if user_input not in base_commands and user_input not in ["attack", "a", "run", "r", "info", "i"]:
            print(invalid_command_prompt)
        elif user_input in ["close", "cl"]:
            close_confirmation()
        elif user_input in ["clear", "c"]:
            clear_terminal()
        elif user_input in ["?", "help", "h"]:
            print(base_command_description)
            print('"attack, a": do an attack\n'
                  '"run, r": attempt to run away\n'
                  '"info, i" shows info about the enemy')
        elif user_input in ["run", "r"]:
            if input("Are you sure? (Anything other than yes will be counted as no) >> ").lower() == "yes":
                if random.randint(0, 100) > 60:
                    print("You escaped sucsefully")
                    return "ran away"
                else:
                    print("You failed to escape")
                    continue
            else:
                continue
        elif user_input in ["attack", "a"]:
            return "attack"
        elif user_input in ["info", "i"]:
            for k, v in enemy.items():
                if type(v) == dict:
                    for k, v in enemy["stats"].items():
                        print(f"{k}: {v}")
                else:
                    print(f"{k}: {v}")


def attack_combat_input():
    while True:
        user_input = input(
            "What move do you want to use? (type ? for a list of commands) >> ").lower()
        if user_input in user_moves:
            deal_damage(enemy, damage_formula('enemy',
                                              enemy["stats"]["defense"], user_data["stats"]["attack"], moves[user_input]["move_damage"]))
            print(
                f"Used {user_input} enemy hp is now {0 if enemy['hp'] < 1 else enemy['hp']}")
            if enemy["hp"] < 1:
                print(f"You beat the {enemy["name"]}!")
                break
            return 'attacked'
        elif user_input not in user_moves and user_input not in base_commands and user_input not in ["cancel", "ca", "?", "show", "s", "info", "i"]:
            print(invalid_command_prompt)
        elif user_input in ["close", "cl"]:
            close_confirmation()
        elif user_input in ["cancel", "ca"]:
            break
        elif user_input in ["clear", "c"]:
            clear_terminal()
        elif user_input in ["?", "help", "h"]:
            print(base_command_description)
            print('"cancel, c": cancel doing an attack\n'
                  '"show, "s: shows moves you can use\n'
                  '"info, i": shows info about the enemy')
        elif user_input in ["show", "s"]:
            print(f"You can use {', '.join(user_moves)}")
        elif user_input in ["info", "i"]:
            for k, v in enemy.items():
                if type(v) == dict:
                    for k, v in enemy["stats"].items():
                        print(f"{k}: {v}")
                else:
                    print(f"{k}: {v}")
