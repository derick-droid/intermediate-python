"""
Create the following lists using a for loop.
(a) A list consisting of the integers 0 through 49
(b) A list containing the squares of the integers 1 through 50.

"""


def six_b():
    list_value = []
    for item in range(51):
        list_value.append(item**2)

    print(list_value)


six_b()
    