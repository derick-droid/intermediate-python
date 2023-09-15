"""
Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 4, 5, and 6 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
"""


def three():
    list_value = [8, 9, 10]
    new_list = list_value + [4, 5, 6]
    new_list.remove(8)
    new_list.sort()

    print(new_list)


three()


