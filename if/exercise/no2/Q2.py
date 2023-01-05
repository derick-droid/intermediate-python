"""
Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in. Your program should convert the temperature to the other unit. The conversions
are F =
9
5
C + 32 and C =
5
9
(F − 32).
"""


def two():
    temp = int(input("Enter your temperature: "))
    unit = input("Enter the unit of your temperature(celsius(C)/Fahrenheit(F) :")
    if unit == "C".lower():
        result_fah = ((9/5) * temp) + 32
        print(f" your temperature is{result_fah} in Fahrenheit")

    elif unit == "F":
        result_c = (9 / 5) * (temp - 32)
        print(f" your temperature is {result_c} in celsius")

    else:
        print("Invalid unit")


two()


