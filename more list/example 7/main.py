"""
As we can see, since split breaks up the string at spaces, the punctuation will be part of the
words. There is a module called string that contains, among other things, a string variable called
punctuation that contains common punctuation. We can remove the punctuation from a string s
with the following code:
"""
from string import  punctuation


def punct():
    word = "I am coming home!!!!!!!!!!!"

    for c in punctuation:
        word = word.replace(c, " ")
    print(word)


punct()