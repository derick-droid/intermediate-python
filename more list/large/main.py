"""
Creating large two-dimensional lists
"""


def large():
    new_list = [[0] * 50 for i in range(100)]

    print(new_list)


large()
