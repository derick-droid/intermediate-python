"""
(c) The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.
"""

l = []

for i in range(1, 27):
    l.append(chr(i + 96) * i)

print("Created List:")

print(l)

