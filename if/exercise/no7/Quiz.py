"""
Write a program that asks the user for two numbers and prints Close if the numbers are
within .001 of each other and Not close otherwise.
"""


def numbers():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter second number: "))
    sub = abs(number1 - number2)

    if sub <= 0.001:
        print("Close")
    else:
        print("Otherwise")


numbers()
