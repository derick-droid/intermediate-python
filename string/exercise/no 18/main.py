"""
The goal of this exercise is to see if you can mimic the behavior of the in operator and the
count and index methods using only variables, for loops, and if statements.
(a) Without using the in operator, write a program that asks the user for a string and a letter
and prints out whether or not the letter appears in the string.
(b) Without using the count method, write a program that asks the user for a string and a
letter and counts how many occurrences there are of the letter in the string.
(c) Without using the index method, write a program that asks the user for a string and
a letter and prints out the index of the first occurrence of the letter in the string. If the
letter is not in the string, the program should say so.

"""


def eighteen():
    word = input("Enter a string: ")
    letter = input("Enter a letter: ")
    flag = 0
    for item in word:
        if item == letter:
            flag = 1
    if flag == 1:
        print("The letter is in the word")
    else:
        print("The letter is not in the word")


eighteen()


# b
def eighteenII():
    word = input("Enter a word: ")
    letter = input("Enter a letter: ")
    count = 0
    for item in word:
        if item == letter:
            count += 1

    print(count)

eighteenII()