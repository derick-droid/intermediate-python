"""
(a) Write a program that asks the user to enter a sentence and then randomly rearranges the
words of the sentence. Don’t worry about getting punctuation or capitalization correct.
"""

from random import shuffle


def fix():
    sentence = input("Enter a sentence: ")
    new_list = list(sentence.split(" "))
    shuffle(new_list)

    new_sentence = " ".join(new_list)
    print(new_sentence)


fix()


