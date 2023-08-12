"""

A more general version of the above technique is the rail fence cipher, where instead of break-
ing things into evens and odds, they are broken up by threes, fours or something larger. For
instance, in the case of threes, the string secret message would be broken into three groups. The
first group is sr sg, the characters at indices 0, 3, 6, 9 and 12. The second group is eemse, the
characters at indices 1, 4, 7, 10, and 13. The last group is ctea, the characters at indices 2, 5, 8,
and 11. The encrypted message is sr sgeemsectea.
(a) Write a program the asks the user for a string and uses the rail fence cipher in the threes
case to encrypt the string.
(b) Write a decryption program for the threes case.
(c) Write a program that asks the user for a string, and an integer determining whether to
break things up by threes, fours, or whatever. Encrypt the string using the rail-fence
cipher.
(d) Write a decryption program for the general case.


"""

