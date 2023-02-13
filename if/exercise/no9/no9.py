"""
Write a program that asks the user to enter a number and prints out all the divisors of that
number. [Hint: the % operator is used to tell if a number is divisible by something. See Section
3.2.]
"""


def number():
    list = []
    num = int(input("Enter a number: "))
    for digit in range(1, num+1):
        if num % digit == 0:
            list.append(digit)

    for item in list:
        print(item)


number()
