"""

Write a program that removes any repeated items from a list so that each item appears at most
once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
"""

def thirteen():

    l = [1,1,2,3,4,3,0,0]
    new_l = []

    for i in l:
        if i in new_l:
            pass
        else:
            new_l.append(i)

    print(new_l)


thirteen()


