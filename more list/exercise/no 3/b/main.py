"""
(a) Ask the user to enter a sentence and print out the third word of the sentence.
"""


def third():
    L = []
    sentence = input("Enter a sentence:  ")

    for item in sentence:
        L.append(item)
        print(item)

    print(L)

    print(L[3])


third()
