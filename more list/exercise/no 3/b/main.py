"""
(a) Ask the user to enter a sentence and print out the third word of the sentence.
"""


def third():
    sentence = input("Enter a sentence:  ")
    new_list = list(sentence.split(" "))

    print(new_list[3])



third()
