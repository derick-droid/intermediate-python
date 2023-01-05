

"""
Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an
inch.
"""


def one():
    length = int(input("Enter your length in Centimetres(cm): "))
    if length < 0:
        print("The entry you have entered is invalid")

    else:
        result = length/2.54
        print(f" your lenght is {result} in inches")


one()