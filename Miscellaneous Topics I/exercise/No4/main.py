"""
Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000.
"""

def four():
    sum = 0
    for i in range(1, 20001):
        sum = sum + i
    print(sum)

four()
