"""
People often forget closing parentheses when entering formulas. Write a program that asks
the user to enter a formula and prints out whether the formula has the same number of opening and closing parentheses.

"""


def three():
    formula = input("Enter a formula: ")
    count = 0
    for item in formula:
        if item == "(":
            count += 1
        elif item == ")":
            count -= 1

    if count == 1:
        print("The formula has no all paranthesis ")
    elif count == 0:
        print("the formula has all paranthesis")




three()