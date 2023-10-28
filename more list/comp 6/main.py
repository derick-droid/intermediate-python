"""
Example 1 Write a program that generates a list L of 50 random numbers between 1 and 100.

"""
from random import  randint
L = [randint(1,100) for i in range(50)]

print(L)