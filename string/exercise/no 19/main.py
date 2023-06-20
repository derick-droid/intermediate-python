"""
Write a program that asks the user for a large integer and inserts commas into it according
to the standard American convention for commas in large numbers. For instance, if the user
enters 1000000, the output should be 1,000,000.

"""


def nineteen():
    number = input("Enter a large integer: ")
    if len(number) >= 4:
        res = '{:,}'.format(int(number))
        print(res)


nineteen()
