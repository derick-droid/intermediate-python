"""
. Ask the user to enter a temperature in Celsius. The program should print a message based
on the temperature:
• If the temperature is less than -273.15, print that the temperature is invalid because it is
below absolute zero.
• If it is exactly -273.15, print that the temperature is absolute 0.
• If the temperature is between -273.15 and 0, print that the temperature is below freezing.
• If it is 0, print that the temperature is at the freezing point.
• If it is between 0 and 100, print that the temperature is in the normal range.
• If it is 100, print that the temperature is at the boiling point.
• If it is above 100, print that the temperature is above the boiling point
"""


def three():
    temp = float(input("Enter your temperature in celsius: "))
    if temp < -273.15:
        print("temperature is invalid because it is below absolute zero")
    elif temp == -273.15:
        print("temperature is absolute 0.")
    elif temp == -273.15 or temp < 0:
        print("Temperature is below freezing point")

    elif temp == 0:
        print("Temperature is at freezing point")

    elif temp == 0 or temp <= 100:
        print("Temperature is at normal range")

    elif temp == 100:
        print("Temperature is at Boiling point")

    elif temp > 100:
        print("Temperature is above boiling point")


three()
