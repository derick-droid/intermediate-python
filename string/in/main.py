s = " "
for i in range(10):
    t = input("Enter a letter: ")
    if t == "a" or t == "e" or t == "i" or t == "o" or t == "u":
        s = s + t

if "a" in s:
    print("character a is string")

print(s)
