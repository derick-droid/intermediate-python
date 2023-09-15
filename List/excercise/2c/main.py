"""
Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.

"""
import random
from random import randint

list_value = []


def two():
    for num in range(20):
        new_number = random.randint(1, 100)
        list_value.append(new_number)

    print(f"{max(list_value)} is the largest value in the list")
    print(f"{min(list_value)} is the smallest value in the list ")


two()


