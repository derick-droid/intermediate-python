"""
Example 2 Write a program that asks the user for a string and prints out the location of each 'a'
in the string.

word = input("Enter a word: ")
for item in range(len(word)):
    if word[item] == "a":
        print(item)
"""

word = input("Enter a word: ")
for item in range(len(word)):
    if word[item] == "a":
        print(item)