"""
Write a program that creates an anagram of a given word. An anagram of a word uses
the same letters as the word but in a different order. For instance, two anagrams of the word there
are three and ether. Don’t worry about whether the anagram is a real word or not.
"""

from random import shuffle


def join_list():
    word = input("Enter a word: ")
    letter_list = list(word)
    shuffle(letter_list)

    anagram = " ".join(letter_list)

    print(anagram)


join_list()