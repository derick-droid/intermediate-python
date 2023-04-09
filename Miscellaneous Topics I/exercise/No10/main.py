"""
. Ask the user to enter 10 test scores. Write a program to do the following:
(a) Print out the highest and lowest scores.
(b) Print out the average of the scores.
(c) Print out the second largest score.
(d) If any of the scores is greater than 100, then after all the scores have been entered, print
a message warning the user that a value over 100 has been entered.
(e) Drop the two lowest scores and print out the average of the rest of them
"""


def ten():

    summ = 0
    flg = 0
    average = 0

    list_1 = []
    for i in range(10):
        num = int(input("Enter scores: "))
        list_1.append(num)
        summ = summ + num
        average = summ / 10

    print(f"The average of score is {average}")

    # finding the greater number
    for item in list_1:
        if item > 100:
            flg = 1
    if flg == 1:
        print("A value greater than 100 has been entered")

#     finding the highest and lowest value
    highest_score = list_1[0]
    lowest_score = list_1[0]
    for number in list_1:
        if number > highest_score:
            highest_score = number
    print(f"{highest_score} is the largest score")

    for n in list_1:
        if n < lowest_score:
            lowest_score = n

    print(f"{lowest_score} is the lowest score")
# finding second largest
    list_sorted = sorted(list_1)
    print(f"{list_sorted[8]} is the second largest number")
    print(list_1)

#     Drop the two lowest scores and print out the average of the rest of them

    del list_sorted[0:2]
    sum_1 = 0
    new_average = 0
    for value in list_sorted:
        sum_1 = sum_1 + value

    new_average = sum_1 / len(list_sorted)
    print(f"the average number of remaining score is {new_average}")


ten()
