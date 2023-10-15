"""
Here is a program that counts how many times a certain word occurs in a string.

"""


from string import punctuation


def seven():
    s = input("Enter a string: ")
    for c in punctuation:
        s = s.replace(c, " ")
    s = s.lower()
    l = s.split()

    word = input("Enter a word: ")

    print(f"{word} appears {l.count(word)} times")


seven()
