"""
Changing lists Changing a specific item in a list is easier than with strings. To change the value
in location 2 of L to 100, we simply say L[2]=100. If we want to insert the value 100 into location
2 without overwriting what is currently there, we can use the insert method. To delete an entry
from a list, we can use the del operator. Some examples are shown below. Assume L=[6,7,8] for
each operation.

"""


def change():
    l = [4, 9, 0]
    l[0] = 100

    print(l)

    l.insert(0, 3)
    print(l)
    del l[0]
    print(l)
    del l[:]

    print(l)
change()