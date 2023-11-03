""""
One more example Suppose we have a list whose elements are lists of size 2, like below:
L = [[1,2], [3,4], [5,6]]
If we want to flip the order of the entries in the lists, we can use the following list comprehension:

"""


def flip():
    L = [[1, 2], [3, 4], [5, 6]]

    new_list = [[y, x] for x, y in L]

    print(new_list)


flip()