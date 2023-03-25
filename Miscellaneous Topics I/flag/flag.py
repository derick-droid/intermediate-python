"""
A flag variable can be used to let one part of your program know when something happens in
another part of the program
"""

# . Here is an example that determines if a number is prime.


def flag():
    flag1 = 0
    num = int(input("Enter number: "))

    for i in range(2, num):
        if (num % i) == 0:
            flag1 = 1

    if flag1 == 1:
        print("The number is not prime number")
    else:
        print("Not prime number")


flag()