"""
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
4 and how many end in a 9.
"""


def two():
    count_1 = 0
    count_2 = 0
    for i in range(1, 101):
        if (i ** 2) % 10 == 4:
            count_1 = count_1 + 1
        elif (i ** 2) % 10 == 9:
            count_2 = count_2 + 1
    print(f"There are {count_1} numbers ending in 4 and {count_2} ending with 9")


two()