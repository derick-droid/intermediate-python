"""

Example 3 Count how many items in a list L are greater than 50.
"""
from random import randint


def grt():
    L = [8, 12, 13, 44, 25, 20, 37, 68, 51, 15, 40, 95, 9, 27, 29, 85, 4,
         87, 20, 82, 32, 49, 70, 16, 13, 46, 35, 52, 44, 46, 5, 21, 98, 1,
         80, 71, 26, 2, 95, 53, 48, 55, 16, 51, 41, 59, 11, 7, 96, 50]
    count = 0
    for item in L:
        if item > 50:
            count = count + 1
    print(f"there are {count} figures greater than 50 in the list")


grt()




