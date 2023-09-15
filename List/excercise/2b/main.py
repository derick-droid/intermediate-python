"""
Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.

"""
import random
from random import randint

list_value = []
sum_value = 0
value = 0


def two():
    for num in range(2):
        new_number = random.randint(1, 100)
        list_value.append(new_number)

    average = sum(list_value) / len(list_value)
    print(average)


two()


