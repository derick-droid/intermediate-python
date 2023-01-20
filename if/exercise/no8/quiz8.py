"""
. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Write a program that asks the user for a year and prints
out whether it is a leap year or not.
"""


def year():
    years = int(input("Enter a year: "))

    if years % 4 == 0 and years % 100 != 0 or years % 400 == 0 :
        print("leap Year")
    else:
        print("Not leap year")

        
year()

