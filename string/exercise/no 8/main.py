"""
At a certain school, student email addresses end with @student.college.edu, while pro-
fessor email addresses end with @prof.college.edu. Write a program that first asks the
user how many email addresses they will be entering, and then has the user enter those ad-
dresses. After all the email addresses are entered, the program should print out a message
indicating either that all the addresses are student addresses or that there were some profes-
sor addresses entered.

"""


def eight():
    number = int(input("How many emails do you want to enter?: "))
    count_student_email = 0
    count_prof_email = 0
    for i in range(number):
        email = input("Enter the emails: ")

        if email[-20:] == "@student.college.edu":
            count_student_email += 1
        elif email[-17:] == "@prof.college.edu":
            count_prof_email += 1

    if count_prof_email > count_student_email:
        print("There are more students emails than professor emails")
    elif count_student_email > count_prof_email:
        print("There are more students emails than professor emails")
    elif count_student_email == count_prof_email:
        print("Both emails are equals")


eight()


