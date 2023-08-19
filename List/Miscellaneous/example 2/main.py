"""

Example 2 Replace each element in a list L with its square.
"""

from random import randint


def rand():
    l = []
    for i in range(50):
        l.append(randint(1, 100))
    # print(l)

    for x in range(len(l)):
        l[x] = l[x] ** 2
    print(l)


rand()
