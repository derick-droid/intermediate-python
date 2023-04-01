"""
Write a program that asks the user to enter a number and prints the sum of the divisors of
that number. The sum of the divisors of a number is an important function in number theory.
"""


def five():
    number = int(input("Enter number: "))
    sum = 0
    for i in range(1, number+1):
        if (number % i ) == 0:
            sum = sum + i
    print(sum)


five()
