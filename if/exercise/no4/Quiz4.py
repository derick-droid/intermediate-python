"""
Write a program that asks the user how many credits they have taken. If they have taken 23
or less, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.
"""


def credits():
    credo = int(input("How many credits do you have? "))
    if credo <= 23:
        print("This student is freshman")
    elif credo == 24 or credo <= 53:
        print("The student is sophomore")

    elif credo == 54 or credo <= 83:
        print("The student is junior")

    elif credo >= 84:
        print("The student is senior")


credits()
