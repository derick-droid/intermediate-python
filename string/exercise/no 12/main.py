""""

Write a program that asks the user to enter a word and then capitalizes every other letter of
that word. So if the user enters rhinoceros, the program should print rHiNoCeRoS.

"""

import random


def twelve():
    word = input("Enter a word: ")
    new_word = ""
    for i in range(len(word)):
        if i % 2 != 0:
            new_word += word[i].upper()
        else:
            new_word += word[i]
    print(new_word)

twelve()
