"""

A simple way of encrypting a message is to rearrange its characters. One way to rearrange the
characters is to pick out the characters at even indices, put them first in the encrypted string,
and follow them by the odd characters. For example, the string message would be encrypted
as msaeesg because the even characters are m, s, a, e (at indices 0, 2, 4, and 6) and the odd
characters are e, s, g (at indices 1, 3, and 5).
(a) Write a program that asks the user for a string and uses this method to encrypt the string.
(b) Write a program that decrypts a string that was encrypted with this method.

"""


def twenty_two():
    word = input("Enter a word: ")
    even = ""
    odd = ""
    for item in range(len(word)):

        if item % 2 == 0:
            even = even + word[item]
        else:
            odd = odd + word[item]
    print(f"{even}{odd}")


twenty_two()


def decrypt():
    string = input('what is your message: ')
    length = len(string)  # to get the length of the input
    half_length = (length + 1) // 2  # half of the input
    even = string[:half_length]  # even part
    odd = string[half_length:]  # odd part

    msg = ""


decrypt()
