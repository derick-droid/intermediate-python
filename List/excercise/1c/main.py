"""
Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.

"""


def enter():

    list = []
    for num in range(15):
        number = input("Enter interger: ")
        list.append(number)

    print(list)
    print(list[-1])


enter()
