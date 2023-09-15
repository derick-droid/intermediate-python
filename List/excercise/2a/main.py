"""
Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.

"""
import random
from random import randint

list = []
def two():
    for num in range(20):
        new_number = random.randint(1, 100)
        list.append(new_number)

    print(list)

two()


