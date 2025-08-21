#Grade calculator of a student

#Getting marks from the user,each subject is upto 100 marks.
"""first_subject = int(input("Enter marks for the first subject:"))
second_subject = int(input("Enter marks for the second subject:"))
third_subject = int(input("Enter marks for the third subject:"))
fourth_subject = int(input("Enter marks for the fourth subject:"))
fifth_subject = int(input("Enter marks for the fifth subject:"))"""

"""instead of getting each subject marks without validation..we can get each subject with validation  using function"""
def get_marks(subject_name): 
    while True:
        marks = int(input(f"Enter marks for {subject_name} (0-100):"))
        if (marks >=0 and marks <= 100):
            return marks
        else:
            print("Invalid marks.Please enter valid marks (0-100).")

first_subject=get_marks("subject_1")
second_subject=get_marks("subject_2")
third_subject=get_marks("subject_3")
fourth_subject=get_marks("subject_4")
fifth_subject=get_marks("subject_5")

#Calculating percentage
sum = first_subject+second_subject+third_subject+fourth_subject+fifth_subject
percentage = (sum/500) * 100

#Assigning grades based on percentage
if(percentage > 100):
    print("Invalid percentage")
elif (percentage >= 90 and percentage <= 100):
    print(f"You got {percentage:.2f}% which leads to \"A\" grade")
elif(percentage >= 75 and percentage < 90):
    print(f"You got {percentage:.2f}% which leads to \"A-\" grade")
elif(percentage >= 60 and percentage < 75):
    print(f"You got {percentage:.2f}% which leads to \"B+\" grade")
elif(percentage >= 50 and percentage <60):
    print(f"You got {percentage:.2f}% which leads to \"B\" grade")
elif(percentage >= 40 and percentage < 50):
    print(f"You got {percentage:.2f}% which leads to \"C\" grade")
else:
    print(f"You got {percentage:.2f}% which leads to \"F\" grade")