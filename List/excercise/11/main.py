"""
Using a for loop, create the list below, which consists of ones separated by increasingly many
zeroes. The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

"""


def eleven():
    L = [1]
    for i in range(11):
        if i == 0:
            L.append(1)
        else:
            for j in range(i):
                L.append(0)
            L.append(1)
    print(L)


eleven()
