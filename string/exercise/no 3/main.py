"""
People often forget closing parentheses when entering formulas. Write a program that asks
the user to enter a formula and prints out whether the formula has the same number of opening and closing parentheses.

"""


def three():
    formula = input("Enter a formula: ")
    if "(" and ")" in formula:
        print("All paranthesis are available")

three()