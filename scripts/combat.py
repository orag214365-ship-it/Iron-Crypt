import random
from variables import enemy
from inputs import base_combat_input


def combat():
    while True:
        print(f"You found a {enemy['name']}")
        combat_user_input = base_combat_input()

        if combat_user_input == "attack":
            print("i did not program this yet")
            break
        elif combat_user_input == "ran away":

            break
