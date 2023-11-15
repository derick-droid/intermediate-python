"""
Picking out rows and columns To get the r th row of L, use the following:
To get the c th column of L, use a list comprehension:
"""


def position():
    L = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    new = [L[i] for i in range(len(L))]

    print(new)


position()
