"""

An integer is called squarefree if it is not divisible by any perfect squares other than 1. For
instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
tells them if it is squarefree or not.

"""

import math


def seven():
    flag = 0
    num = int(input("Enter a number: "))
    for i in range(2, num + 1):
        square_root = math.sqrt(i)
        if square_root == int(square_root):
            flag = 1

    if flag == 1:
        print(f"{num} is a square free number ")
    else:
        print(f"{num} is not a square free number")


seven()




