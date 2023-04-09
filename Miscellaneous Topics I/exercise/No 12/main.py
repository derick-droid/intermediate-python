"""
Write a program that asks the user to guess a random number between 1 and 10. If they guess
right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give
the user five numbers to guess and print their score after all the guessing is done.

"""


import random


def twelve():
    score = 0
    guess = random.randint(1, 10)
    for i in range(5):
        num = int(input("Enter a random number between (1, 10): "))
        if (num < 1 or  num > 10):
            print("Invalid input")
        elif num == guess:
            score = score + 10
        elif guess != num:
            score = score - 1
    if score < 0:
        print(f"You have lost the game, your score is {score}")
    else:
        print(f"You have a positive score of {score}")




twelve()


