"""
Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect
cubes, or perfect fifth powers.
"""
import  math
def nine():
    count_1 = 0
    count_2 = 0
    count_3 = 0

    for i in range(1, 1000):
        square_root = math.sqrt(i)
        cube_root = (i ** 1/3)
        fifth_root = (i ** 1/5)
        if square_root != int(square_root):
            count_1 = count_1 + 1
        elif cube_root != int(cube_root):
            count_2 = count_2 + 1
        elif fifth_root != int(fifth_root):
            count_3 = count_3 + 1

    print(f" we have {count_1} not perfect squares")
    print(f" we have {count_2} not perfect cubes")
    print(f" we have {count_3}  not perfect fifth")


nine()

