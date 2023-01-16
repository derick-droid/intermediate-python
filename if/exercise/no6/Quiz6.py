"""
A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
program that asks the user how many items they are buying and prints the total cost.
"""


def charges():
    item = int(input("How many items do you want to buy: "))
    if item < 10:
        print(item * 12 )
    elif item == 10 or item < 99:
        print(item * 10)
    elif item >= 100:
        print(item * 7)




charges()