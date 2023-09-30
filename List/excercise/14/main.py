"""

Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists.

"""


def fourteen():
    feet = input("Enter feet : ")

    print("""
         Choose 0 to convert into inches,
          choose 1 to convert into yards,
          choose 2 to convert into miles,
          choose 3 to convert into millimeters,
          choose 4 to convert into centimeters,
          choose 5 to convert into meters,
          choose 6 to convert into kilometers
    
    """)

    integer = int(input("Enter the integer: "))
    if integer > 6:
        print("The number of limit of the list")

    else:
        inches = feet * 12
        yards = feet * int(0.33333)
        miles = feet * int(0.000189393939)
        millimeters = feet * int(304.8)
        centimeters = feet * int(30.48)
        meters = feet * int(0.3048)
        kilometers = feet * int(0.0003048)

        convert = [inches, yards, miles, millimeters, centimeters, meters, kilometers]

        print(convert[integer])


fourteen()

