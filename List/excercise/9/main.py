"""
When playing games where you have to roll two dice, it is nice to know the odds of each
roll. For instance, the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about
17%. You can compute these mathematically, but if you don’t know the math, you can write
a program to do it. To do this, your program should simulate rolling two dice about 10,000
times and compute and print out the percentage of rolls that come out to be 2, 3, 4, . . . , 12.

"""


def nine():
    from random import randint
    dice_roll = []
    outcome = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    sim = 10

    for simulations in range(sim):
        first_dice_roll = randint(1, 6)
        second_dice_roll = randint(1, 6)

        dice_roll.append(first_dice_roll + second_dice_roll)
        sumi = sum(dice_roll)
    print(dice_roll, "Dice roll")


nine()