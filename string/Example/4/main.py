"""
Example 4 Write a program that asks a user for their name and prints it in the following funny
pattern:
E El Elv Elvi Elvis
"""
name = input("Enter name: ")
for item in range(len(name)):
    print(name[:item + 1], end=" ")
