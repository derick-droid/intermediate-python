"""
Write a program that asks the user to enter a word and prints out whether that word contains
any vowels.

"""


def vowel():
    word = input("Enter a word: ")
    flag = 0
    for item in word:
        if item == "a" or item == "e" or item == "i" or item == "o" or item == "u":
            flag = 1
        else:
            flag = 0

    if flag == 1:
        print("There are  vowels in the word ")
    elif flag == 0:
        print("There are no vowels in the word")


vowel()

