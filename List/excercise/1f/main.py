"""
Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the
result.

"""


def enter():

    list = []
    available_five = 0
    for num in range(5):
        number = int(input("Enter integer: "))
        list.append(number)

    del list[0]
    del list[-1]
    print(list)

enter()

