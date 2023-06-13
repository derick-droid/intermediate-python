"""
Write a program that asks the user to enter a string. The program should create a new string
called new_string from the user’s string such that the second character is changed to an
asterisk and three exclamation points are attached to the end of the string. Finally, print
new_string. Typical output is shown below:
Enter your string: Qbert
Q*ert!!!

"""


def five():
    word = input("Enter a string: ")
    if len(word) >= 3:
        new_string = word.replace(word[1], "!") + "!!!"
        print(new_string)
    else:
        print("Your word is less than 3 characters")



five()