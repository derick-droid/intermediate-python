"""
Write a program that asks the user to enter a string. The program should then print the
following:

(k) The string with every letter replaced by a space

"""


def the_k():
    word = input("Enter a word: ")
    word = word.replace(word[:], " ")
    print(word)
    

the_k()

