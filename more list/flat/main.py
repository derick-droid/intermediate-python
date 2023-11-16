"""
Flattening a list To flatten a two-dimensional list, that is, return a one-dimensional list of its
elements, use the following:
"""


def flat():
    L = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    new_list = [j for M in L for j in M]

    print(new_list)


flat()

