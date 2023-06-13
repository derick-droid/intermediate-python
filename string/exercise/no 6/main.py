"""
Write a program that asks the user to enter a string s and then converts s to lowercase, removes all the periods and commas from s,
and prints the resulting string.

"""


def six():
    word = input("Enter a word: ")
    if "." or "," in word:
      word = word.replace(".", "")
      word = word.replace(",", "")

    print(word.lower())

six()