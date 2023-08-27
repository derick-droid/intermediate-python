"""


"""
question = ["What is the capital city of Kenya? : ", "Which is the code for Nairobi county? : "]

answer = ["Nairobi", "047"]

num_right = 0

for i in range(len(question)):
    guess = input(question[i])
    if guess == answer[i]:
        print("correct")
        num_right = num_right + 1

print(num_right)
