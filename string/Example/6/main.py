"""
Write a program that, given a string that contains a decimal number, prints out the
decimal part of the number. For instance, if given 3.14159, the program should print out .14159.

"""
number = (input("Enter a number: "))
print(number[number.index("."):])