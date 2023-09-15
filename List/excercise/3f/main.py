"""
Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 4, 5, and 6 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3
"""


def three():
    list_value = [8, 9, 10]
    new_list = list_value + [4, 5, 6]
    new_list.remove(8)
    new_list.sort()
    Third_list = new_list * 2

    Third_list.insert(3, 25)

    print(Third_list)



three()


