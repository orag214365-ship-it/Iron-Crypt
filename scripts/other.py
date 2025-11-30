import os
import sys
import random
from variables import user_data


def close_confirmation():
    if input("Are you sure? (Anything other than yes will be counted as no) >> ").lower() == "yes":
        sys.exit()
    else:
        pass


def clear_terminal():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


def deal_damage(target, amount):
    if target == 'player':
        target == user_data
    target["hp"] -= amount


def damage_formula(target, defense, attack, movedamage):
    crit_chance = random.randint(0, 100)
    if crit_chance < 5:
        print(f"A citical hit!")
    if target == 'player':
        return 1 if round((movedamage + attack ** 1.3) * (1 if crit_chance > 5 else 2) - (defense ** 0.9)) < 1 else round((movedamage + attack ** 1.3) * (1 if crit_chance > 5 else 2) - (defense ** 0.9) * random.uniform(1.1, 1.5))
    else:
        return 1 if round(((movedamage + attack ** 1.3) * (1 if crit_chance > 5 else 2) - (defense ** 0.9)) / 1.5) < 1 else round(((movedamage + attack ** 1.3) * (1 if crit_chance > 5 else 2) - (defense ** 0.9)) / 1.5 * random.uniform(1.1, 1.5))
