def word_list():
    M = ['one ', 'two ', 'three ', 'four ', 'five ', 'six ']

    new_list = [m[0] for m in M if len(m)==3]

    print(new_list)


word_list()
