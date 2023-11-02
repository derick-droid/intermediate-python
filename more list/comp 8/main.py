"""
Example 4 Given a list L that contains numbers between 1 and 100, create a new list whose first
element is how many ones are in L, whose second element is how many twos are in L, etc.
"""

from random import  randint
def count_l():
    L = [randint(1, 100) for i in range(50)]
    frequencies = [L.count(i) for i in range(1, 101)]
    print(frequencies)

count_l()