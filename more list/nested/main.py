""""
Working with two-dimensional lists Nested for loops, like the ones used in printing a two-
dimensional list, can also be used to process the items in a two-dimensional list. Here is an example
that counts how many entries in a 10 × 5 list are even.

"""

L = []


def netse():
    count = 0
    for r in range(10):
        for c in range(5):
            if r % 2 == 0:
                L.append(r)
                count = count + 1
            elif c % 2 == 0:
                count = count + 1
                L.append(c)

    print(count)


netse()
