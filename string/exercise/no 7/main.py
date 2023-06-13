"""
 Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards.
"""


def seven():
    word = input("Enter a word: ").lower()
    if word == word[:: -1]:
        print("The word is palindrome")
    else:
        print("The word you have entered is not palindrome")


seven()
