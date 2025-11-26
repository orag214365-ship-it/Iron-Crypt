import sys
import os


def comabt_input():
    while True:
        user_input = input(
            "What do you want to do? (Type ? for a list of commands) >> ").lower()
        if user_input not in ["close", "cl", "?", "help", "h", "attack", "a", "run", "r", "clear", "c"]:
            print("Please type a valid command. (Type ? for a list of commands)")
        elif user_input in ["close", "cl"]:
            if input("Are you sure? (Anything other than yes will be counted as no) >> ").lower() == "yes":
                sys.exit()
            else:
                continue
        elif user_input in ["clear", "c"]:
            if os.name == "nt":
                _ = os.system("cls")
            else:
                _ = os.system("clear")
        elif user_input in ["?", "help", "h"]:
            print('"Close, c": Closes the game')


comabt_input()
