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

