"""
Write a program that computes the factorial of a number. The factorial, n!, of a number n is the
product of all the integers between 1 and n, including n. For instance, 5! = 1 · 2 · 3 · 4 · 5 = 120.
[Hint: Try using a multiplicative equivalent of the summing technique.]

"""


def eleven():
    multicate = 1
    num = int(input("Enter number: "))
    for i in range(1, num + 1):
        multicate = multicate * i

    print(multicate)

eleven()
