"""
Closely related to counting is summing, where we want to add up a bunch of numbers.
"""

# This program will add up the numbers from 1 to 100. The way this works is that each
# time we encounter a new number, we add it to our running total, s.


def sum_up():
    s = 0
    for i in range(1, 101):
        s = s + i
    print(f"the sum of number are {s} ")


sum_up()

"""
Example 2 This program that will ask the user for 10 numbers and then computes their average.
"""


def example_2():
    s1 = 0
    average = 0
    for z in range(10):
        num = int(input("Enter number: "))
        s1 = s1 + z
        average = s1 / 10

    print(average)


example_2()






