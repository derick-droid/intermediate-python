"""
Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the
result.
(g) Print how many integers in the list are less than 5.
"""


def enter():

    list = []
    available_five = 0
    for num in range(5):
        number = int(input("Enter integer: "))
        list.append(number)
    for number in list:
        if number < 5:
            available_five = available_five + 1

    print(f"there are {available_five} less than 5")


enter()



