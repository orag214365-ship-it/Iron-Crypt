import sys
import os


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
