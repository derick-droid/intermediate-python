"""
Example 2 Replace each element in a list L with its square.
L = [i**2 for i in L]
"""

from random import  randint
L = [randint(1,100) for i in range(50)]

new_list = [i**2 for i in L]

print(new_list)