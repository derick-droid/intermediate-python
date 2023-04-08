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
    highest_score = 0
    lowest_score = 0
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
   print()


ten()
