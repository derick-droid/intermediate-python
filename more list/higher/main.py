"""
Higher dimensions Creating and using 3-dimensional and higher lists is similar. Here we create
a 5 × 5 × 5 list:
"""


def higher():
    L = [[[0] * 50 for i in range(5)] for j in range(5)]

    print(L)


higher()
