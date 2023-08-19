"""

Example 4 Given a list L that contains numbers between 1 and 100, create a new list whose first
element is how many ones are in L, whose second element is how many twos are in L, etc.

"""
count_1 = 0
count_2 = 0

L = []

for i in range(1, 100):
    L.append(L.count(i))
frequencies = []
for i in range(1,101):
    frequencies.append(L.count(i))

print(frequencies)