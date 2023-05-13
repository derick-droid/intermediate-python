"""
Write a program that asks the user to enter a string. The program should then print the
following:

(h) The string with its first and last characters removed

"""


def the_h():
    word = input("Enter your a word: ")
    word = word.removeprefix(word[0])
    word = word.removesuffix(word[-1])
    print(word)


the_h()

