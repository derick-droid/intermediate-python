"""
Write a program that asks the user to enter a string, then prints out each letter of the string
doubled and on a separate line. For instance, if the user entered HEY, the output would be
HH
EE
YY

"""


def ten():
    word = input("Enter a word: ").upper()
    for i in (word):
        print(i,i)

ten()