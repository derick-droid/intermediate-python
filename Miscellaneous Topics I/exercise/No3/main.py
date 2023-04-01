"""
Write a program that asks the user to enter a value n, and then computes (1+
1
2 +
1
3 +···+
1
n
)−
ln(n). The ln function is log in the math module.
"""
from math import log


def three():
    n = int(input("Enter number: "))
    summmation= 1
    for i in range(1, n+1):
        result = 1/i
        summmation = summmation + result

    log_value = summmation - log(n)
    print(log_value)


three()

