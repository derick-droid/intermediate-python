"""

Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
entries in the list that are greater than 10 with 10.
"""


def four():
    value = 12
    list_value = []
    for number in range(value):
        num = int(input("Enter a number not less than 1 and not greater than 12: "))

        if num < 1 or num > 12:
            print("Enter a number within the range of 1 to 12")
            value = value + 1

        else:
            list_value.append(num)

    for item in list_value:
        if item > 10:
        
            list_value[list_value.index(item)] = 10

    print(list_value)


four()
