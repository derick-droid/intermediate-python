"""
Write a program that generates 100 random integers that are either 0 or 1. Then find the
longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

"""


import random
sequence = []


def define_sequence():
    for i in range(0, 100):
        sequence.append(random.randint(0, 1))
    print(sequence)


define_sequence()


def sequence_count():
    zero_count = 0  # counts the number of zeros so far
    max_zero_count = 0  # counts the maximum number of zeros seen so faz
    for i in sequence:
        if i == 0:  # if i == 0 we increment both zero_count and max_zero_count
            zero_count += 1
            if zero_count > max_zero_count:
                max_zero_count = zero_count   # if the zero_count is more than the previous max_zero_count we assignt to max_zero_count the zero_count value
        else:
            zero_count = 0  # if i == 1 we reset the zero_count variable
    return max_zero_count


print(sequence_count())
