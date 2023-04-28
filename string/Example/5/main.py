"""
Write a program that removes all capitalization and common punctuation from a
string s.

"""
s = "Cx5523&jjrj"
s = s.lower()

for c in "&*£":
    s = s.replace(c, "")

print(s)
