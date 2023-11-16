"""
Write a program that asks the user to enter some text and then counts how many articles are
in the text. Articles are the words 'a', 'an', and 'the'.
"""


def article():
    count = 0
    content = ["a", "an", "the"]
    text = input("Enter some text: ")
    for item in text:
        if item in content:
            count = count + 1

    print(count)


article()
