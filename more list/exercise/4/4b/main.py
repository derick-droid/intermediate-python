"""
(b) Do the above problem, but now make sure that the sentence starts with a capital, that
the original first word is not capitalized if it comes in the middle of the sentence, and
that the period is in the right place.
"""

from  random import  shuffle

def frixrange():

    sentence = input("Enter a sentence: ")
    new_list = list(sentence.split(" "))
    shuffle(new_list)

    anagram = " ".join(new_list)

    print(anagram.capitalize())


frixrange()