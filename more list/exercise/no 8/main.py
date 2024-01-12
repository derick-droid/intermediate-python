"""
Write a program that simulates drawing names out of a hat. In this drawing, the number of
hat entries each person gets may vary. Allow the user to input a list of names and a list of
how many entries each person has in the drawing, and print out who wins the drawing.

"""

import random


def hat_lottery():
    hat = []

    for name in range(10):
        names = input("Enter name: ")

        hat.append(names)

    right_choice = random.choices(hat)

    random.shuffle(hat)

    computer_choice = random.choices(hat)

    if right_choice == computer_choice:
        print(f"yes you have won the answer is {computer_choice}")

    else:
        print(f" No {right_choice} is not the answer")


hat_lottery()
