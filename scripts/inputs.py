
import random
from variables import user_moves, invalid_command_prompt, enemy, moves, user_data
from other import close_confirmation, clear_terminal, deal_damage


def base_combat_input():
    while True:
        user_input = input(
            "What do you want to do? (Type ? for a list of commands) >> ").lower()
        if user_input not in ["close", "cl", "?", "help", "h", "attack", "a", "run", "r", "clear", "c"]:
            print(invalid_command_prompt)
        elif user_input in ["close", "cl"]:
            close_confirmation()
        elif user_input in ["clear", "c"]:
            clear_terminal()
        elif user_input in ["?", "help", "h"]:
            print('"Close, cl": closes the game\n'
                  '"?, help, h": shows this list\n'
                  '"attack, a": do an attack\n'
                  '"run, r": attempt to run away\n'
                  '"clear, c": clears the terminal')
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


def attack_combat_input():
    while True:
        user_input = input(
            "What move do you want to use? (type ? for a list of commands) >> ").lower()
        if user_input in user_moves:
            deal_damage(enemy, round((moves[user_input]["move_damage"] * (user_data["stats"]["attack"] ** 1.1)) / (
                enemy["stats"]["defense"] ** 0.9)))
            print(f"Used {user_input} enemy hp is now {enemy["hp"]}")
            break
        elif user_input not in [user_moves, "close", "cl", "cancel", "ca", "clear", "c", "?", "help", "h", "show", "s"]:
            print(invalid_command_prompt)
        elif user_input in ["close", "cl"]:
            close_confirmation()
        elif user_input in ["cancel", "ca"]:
            break
        elif user_input in ["clear", "c"]:
            clear_terminal()
        elif user_input in ["?", "help", "h"]:
            print('"close, cl": closes the program\n'
                  '"cancel, ca": go back\n'
                  '"clear, c": clears the terminal\n'
                  '"?, help, h": shows this list\n'
                  '"show, s": shows moves you can use'
                  )
        elif user_input in ["show", "s"]:
            print(f"You can use {', '.join(user_moves)}")


attack_combat_input()
