"""
miscellaneous topics in python
"""


#  count
def counting():
    count = 0
    for i in range(10):
        num = int(input("Enter number: "))
        if num > 10:
            count = count + 1

    print(f"there are {count} greater than 10.")


counting()

