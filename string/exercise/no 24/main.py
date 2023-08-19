"""

In calculus, the derivative of x 4 is 4x 3 . The derivative of x 5 is 5x 4 . The derivative of x 6 is
6x 5 . This pattern continues. Write a program that asks the user for input like x^3 or x^25
and prints the derivative. For example, if the user enters x^3, the program should print out
3x^2.

"""


def calculus():
    figure = input("Enter a calculus expression: ")
    last_position = str(int(figure[-1]) - 1)  # working on the last index
    print(figure[-1] + figure[:-1] + last_position)


calculus()
