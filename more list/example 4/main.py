"""
Example 4 Here is a nice use of shuffle to pick a random ordering of players in a game.
"""
from random import shuffle


def shuffleh():
    names = ["joyce", "goody", "derrick", "okinda"]
    shuffle(names)

    for name in names:
        print(f"{name} it is your turn")


shuffleh()
