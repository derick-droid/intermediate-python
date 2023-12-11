"""
Write a simple lottery drawing program. The lottery drawing should consist of six different
numbers between 1 and 48.
"""


from random import choices


def lottery():
    full_list = []
    lottery_list = []
    for num in range(1, 49):
        full_list.append(num)

    # choosing the lottery
    for times in range(6):
        choice_lottery = choices(full_list)
        lottery_list.append(choice_lottery)

    print(lottery_list)


lottery()
