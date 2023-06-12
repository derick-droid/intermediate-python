"""
Write a program that asks the user to enter a string. The program should then print the
following:
(g) The seventh character of the string if the string is long enough and a message otherwise

"""


def the_g():
    word = input("Enter a string: ")
    if len(word) >= 7:
        print(word[7])
    else:
        print("The character is not available")


the_g()
