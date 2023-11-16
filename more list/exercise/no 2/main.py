"""
Write a program that allows the user to enter five numbers (read as strings). Create a string
that consists of the user’s numbers separated by plus signs. For instance, if the user enters 2,
5, 11, 33, and 55, then the string should be '2+5+11+33+55'.
"""


def replace():
    number = input("Enter five number: ")

    if len(number) < 5:
        print("please enter more number")
    else:
        new_list = []
        for item in number:
            new_list.append(item)
        for num in new_list:
            if num == ",":
                value = new_list.index(num)
                new_list[value] = "+"

        print(new_list)


replace()





