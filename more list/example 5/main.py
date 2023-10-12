"""
Here we use shuffle divide a group of people into teams of two. Assume we are
given a list called names.

"""
from random import shuffle
names = ["denzel", "zebby", "don", "ajax", "dorn"]


def five():
    shuffle(names)
    teams = []

    for i in range(0, len(names), 2):
        teams.append(names[i])

    print(teams)


five()


