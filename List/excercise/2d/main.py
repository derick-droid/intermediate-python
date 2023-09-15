"""
Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list

"""
import random
from random import randint

list_value = []


def two():
    for num in range(20):
        new_number = random.randint(1, 100)
        list_value.append(new_number)

    list_value.sort()
    print(f"{list_value[1]} is the second smallest number in the list")
    print(f"{list_value[-2]} is the second largest number in the list")


two()


