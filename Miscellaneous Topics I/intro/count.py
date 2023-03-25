"""
miscellaneous topics in python
"""


#  count
def counting():
    count = 0
    for i in range(4):
        num = int(input("Enter number: "))
        if num > 10:
            count = count + 1

    print(f"there are {count} greater than 10.")


counting()

"""
Example 2 This modification of the previous example counts how many of the numbers the user
enters are  greater than 10 and also how many are equal to 0. To count two things we use two count
variables.
"""


def greater():
    count1 = 0
    count2 = 0
    for j in range(5):
        num1 = int(input("Enter number: "))
        if num1 > 10:
            count1 = count1 + 1
        elif num1 < 10:
            count2 = count2 + 1
        else:
            print("Invalid entry")
    print(f"there are {count1} numbers  greater than 10 and {count2} numbers less than 10")


greater()

""""
This program counts how many of the squares from 12
to 1002
end in a 4
"""


def count3():
    count3s = 0
    for x in range(1, 101):
        if (x ** 2) % 10 == 4:
            count3s = count3s + 1

    print(count3s)


count3()


