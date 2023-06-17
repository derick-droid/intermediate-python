"""
Write a program that generates the 26-line block of letters partially shown below. Use a loop
containing one or two print statements.
abcdefghijklmnopqrstuvwxyz
bcdefghijklmnopqrstuvwxyza
cdefghijklmnopqrstuvwxyzab
...
yzabcdefghijklmnopqrstuvwx
zabcdefghijklmnopqrstuvwxy

"""


def seventeen():
    """
    This program uses a nested loop to generate each line of letters. The outer loop iterates from 0 to 25, representing the index of each letter in the alphabet. The inner loop iterates from 0 to 25 as well, representing the position of each letter in the line.

Inside the inner loop, we calculate the index of the letter by adding the outer loop index (i) and the inner loop index (j), modulo 26 (the number of letters in the alphabet). We convert the index back to a character using chr() and add it to the line string.
    :return:
    """
    for i in range(26):
        line = ""
        for j in range(26):
            line += chr((i + j) % 26 + ord('a'))
        print(line)





seventeen()



