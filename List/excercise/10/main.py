"""
Write a program that rotates the elements of a list so that the element at the first index moves
to the second index, the element in the second index moves to the third index, etc., and the
element in the last index moves to the first index.

"""


def ten():
    list_value = input("Enter the list: ")
    list_value = list_value[-1] + list_value[:-1]

    print(list_value)


ten()
