"""
Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.

"""


def enter():

    list = []
    available_five = 0
    for num in range(5):
        number = int(input("Enter integer: "))
        list.append(number)

    for number in list:
        if number == 5:
            available_five = available_five + 1

    if available_five == 0:
        print("NO")
    elif available_five >= 1:
        print("YES")


enter()
