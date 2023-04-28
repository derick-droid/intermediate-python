"""
string methods
"""
s = "coming home"

print(s.upper())
print(s.index("c"))
print(s.count(" "))

"""
isalpha
"""
word = input("Enter name: ")
if word[0].isalpha():
    print("The word you have entered starts with a letter")
if not word.isalpha():
    print("The word you have entered is a non letter")

"""
index
"""

if "c" in s:
    print(s.index("c"))

