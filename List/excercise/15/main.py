"""
There is a provably unbreakable cipher called a one-time pad. The way it works is you shift
each character of the message by a random amount between 1 and 26 characters, wrapping
around the alphabet if necessary. For instance, if the current character is y and the shift is 5,
then the new character is d. Each character gets its own shift, so there needs to be as many
random shifts as there are characters in the message. As an example, suppose the user enters
secret. The program should generate a random shift between 1 and 26 for each character.
Suppose the randomly generated shifts are 1, 3, 2, 10, 8, and 2. The encrypted message would
be thebmv.

(a) Write a program that asks the user for a message and encrypts the message using the
one-time pad. First convert the string to lowercase. Any spaces and punctuation in the
string should be left unchanged. For example, Secret!!! becomes thebmv!!! using
the shifts above.

"""

