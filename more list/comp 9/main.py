"""
Another example The join method can often be used with list comprehensions to quickly build
up a string. Here we create a string that contains a random assortment of 1000 letters.
"""

from random import  choice
def alpha():
    letter = "abcdefghijklmnopqrstuvwxyz"

    s = "".join([choice(letter) for i in range (1000)])
    print(s)


alpha()