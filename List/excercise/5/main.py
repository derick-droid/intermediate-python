"""
Ask the user to enter a list of strings. Create a new list that consists of those strings with their
first characters removed.

"""


def five():
    value = 5
    list_word = []
    for word in range(value):
        word = input("Enter a string: ")
        if len(word) <= 2:
            print("Please enter a word with more characters")
            value += 1
        new_word = word.replace(word[0], "")
        list_word.append(new_word)

    print(list_word)


five()


