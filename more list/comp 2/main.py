def word_list():
    M = ['one ', 'two ', 'three ', 'four ', 'five ', 'six ']

    new_list = [letter[0] for letter in M if len(letter) >= 3]

    print(new_list)


word_list()