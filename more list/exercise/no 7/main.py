"""
Write a program that estimates the average number of drawings it takes before the user’s
numbers are picked in a lottery that consists of correctly picking six different numbers that
are between 1 and 10. To do this, run a loop 1000 times that randomly generates a set of
user numbers and simulates drawings until the user’s numbers are drawn. Find the average
number of drawings needed over the 1000 times the loop runs.

"""

import random


def simulatory_lottery():

    total_drawing = 0
    simulations = 1000

    # simulation happening here
    for time in range(simulations):
        user_number = set(random.sample(range(1, 11), 6))
        drawing_numbers = set()

        drawings = 0


# drawing happens so long user numbers and drawing_numbers do not match
        while user_number != drawing_numbers:
            drawing_numbers = random.sample(range(1, 11), 6)
            drawings += 1

        total_drawing += drawings

        average_drawing = total_drawing / simulations

        print(average_drawing)


simulatory_lottery()

