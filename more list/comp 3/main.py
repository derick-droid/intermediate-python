"""#
"""

L = []
M = [ 'one', 'two', 'three', 'four', 'five', 'six']
for m in M:
    print(m)
    print(len(m))
    if len(m) == 3:
        L.append(m)
print(L)