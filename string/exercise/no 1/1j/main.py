"""
Write a program that asks the user to enter a string. The program should then print the
following:
(j) The string with every a replaced with an e

"""


def the_j():
    word = input("Enter a word: ")
    word = word.replace("a", "e")
    print(word)


the_j()
