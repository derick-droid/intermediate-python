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

(b) Write a program to decrypt a string encrypted as above.
The reason it is called a one-time-pad is that the list of random shifts should only be used once.
It becomes easily breakable if the same random shifts are used for more than one message.
Moreover, it is only provably unbreakable if the random numbers are truly random, and the
numbers generated by randint are not truly random. For this problem, just use randint,
but for cryptographically safe random numbers, see Section 22.8.

"""


def fifteen():
    from random import randint
    message = input("Enter a message: ")

    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    secret = []
    for character in message.lower():
        if character in alphabet:
            i = randint(0, 26)
            secret.append(alphabet[i])
        else:
            secret.append(character)

    print(''.join(secret))
    """  b. Write a program to decrypt a string encrypted as above. """

    message = list(message)
    i = 0
    secret_rev = []
    for character in secret:
        secret_rev.append(message[i])
        i += 1

    print(''.join(secret_rev))


fifteen()
