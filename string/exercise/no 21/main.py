"""

An anagram of a word is a word that is created by rearranging the letters of the original.
For instance, two anagrams of idle are deli and lied. Finding anagrams that are real words is
beyond our reach until Chapter 12. Instead, write a program that asks the user for a string
and returns a random anagram of the string—in other words, a random rearrangement of the
letters of that string.

"""

from random import choice
from random import randint


def anagram():
    word = input("Enter a word : ")
    length = len(word)
    number = randint(1, length)
    print(word[number] + word[number] + word[:number])


anagram()


