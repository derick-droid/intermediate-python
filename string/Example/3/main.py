"""
Example 3 Write a program that asks the user for a string and creates a new string that doubles
each character of the original string. For instance, if the user enters Hello, the output should be
HHeelllloo.

"""
word = input("Enter a word: ")
for item in word:
    print(item * 2, end="")
