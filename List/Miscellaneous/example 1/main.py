"""
Example 1 Write a program that generates a list L of 50 random numbers between 1 and 100.

"""
from random import randint


def random():

    l = []
    for i in range(50):
        l.append(randint(1, 100))

    print(l)
    l.sort()
    print(l)

random()