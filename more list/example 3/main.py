"""

The choice function also works with strings, picking a random character from a
string. Here is an example that uses choice to fill the screen with a bunch of random characters.

"""

from random import choices
from random import choice


def choice_string():
    s = "aqwrty"
    for i in range(1000):
        print(choice(s), end="")


choice_string()
