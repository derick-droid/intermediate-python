"""
Write a program that asks the user for an integer and creates a list that consists of the factors
of that integer.
"""


def eight():
    list_value = []
    number = int(input("Enter a number: "))
    if number <= 0:
        print("Please enter a number greater than 0")

    for item in range(1, number):
        if number % item  == 0:
            list_value.append(item)

    print(list_value)


eight()


