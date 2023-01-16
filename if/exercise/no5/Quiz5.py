"""
Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.
"""
from random import randint


def ran():
    for i in range(1, 10):
        a = randint(1, 10)

    guess = int(input("Enter your guess between 1 to 10: "))
    if guess == a:
        print("right")
    else:
        print("wrong")
    print(a)


ran()



