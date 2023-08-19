"""
Making copies of lists Making copies of lists is a little tricky due to the way Python handles lists.
Say we have a list L and we want to make a copy of the list and call it M. The expression M=L will
not work for reasons covered in Section 19.1. For now, do the following in place of M=L:
"""


def copy():

    l = [1, 2, 3, 4, 6, 8]

    m = l[:]

    print(m)


copy()