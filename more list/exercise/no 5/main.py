"""
Write a simple quote-of-the-day program. The program should contain a list of quotes, and
when the user runs the program, a randomly selected quote should be printed.

"""

from random import choice


def quote():
    list_quote = ["never give up", "believe in God", "Fools talk too much"]

    new_quote = choice(list_quote)

    print(new_quote)


quote()


    