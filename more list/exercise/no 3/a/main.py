"""
Ask the user to enter a sentence and print out every third word of the sentence.
"""


def good():
    word = input("Enter a sentence: ")
    new_list = list(word.split(" "))
    print(new_list)

    for i in range(2, len(new_list), 3):

        print(new_list[i], end=" ")


good()
