"""
swapping in python
"""


def swap():
    x = 5
    y = 3
    hold = x
    x = y
    y = hold
    print(x)
    print(y)


swap()

#  another alternative


def swap1():
    x = 5
    y = 2
    x, y = y, x
    print(x)
    print(y)

    
swap1()

