"""
Write a program that asks the user to enter two strings of the same length. The program
should then check to see if the strings are of the same length. If they are not, the program
should print an appropriate message and exit. If they are of the same length, the program
should alternate the characters of the two strings. For example, if the user enters abcde and
ABCDE the program should print out AaBbCcDdEe.

"""


def thirteen():
    word = input("Enter a words: ")
    second_word = input("Enter a second word, This word should be of the same length as previous one: ")

    if len(word) == len(second_word):
       for i in range(len(word)):
           print(word[i] + second_word[i], end="")
    else:
        print("The words are not of the same length")


thirteen()
