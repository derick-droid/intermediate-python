"""

Ask the user for a number and then print the following, where the pattern ends at the number
that the user enters.
1
 2
  3
   4
"""


def nine():
    number = int(input("Enter a number : "))
    for i in range(1, number + 1):
        space = " " * (i - 1)
        print(f"{space}{i}")


nine()
