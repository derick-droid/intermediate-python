"""
Ask the user to enter a sentence and print out every third word of the sentence.
"""


def good():
    word = input("Enter a sentence: ")
    new_list = list(word.split(" "))
    print(new_list)
    print(new_list[4])
    for i in range(0, len(word), 3):
        print(i)
        # print(new_list[i], end=" ")


good()
