##1. Student Score Processor 
##Scenario: 
##A teacher stores student names and marks in a list of tuples. 
##Task: 
##● Convert data into a dictionary 
##● Use a loop + condition to find students scoring above 50 
##● Use math module to calculate average 
##● Store results in a text file 


import math

students = [
    ("Juhi", 85),
    ("Vijay", 45),
    ("Ravi", 65),
    ("priya", 90),
    ("Anu", 40)

]

# Conver list of tuples into dictionary
student_dict = dict(students)

print("Student Details:", student_dict)

#Find students scoring above 50
print("\nStudents scoring above 50:")

for name, marks in student_dict.items():
    if marks > 50:
        print(name, marks)


#Calculate average

total = sum(student_dict.values())
average = math.floor(total / len(student_dict))

print("\nAverage Marks:", average)

#Store results in file

with open("student_result.txt", "w") as file:
    file.write(str(student_dict))
    file.write("\nAverage Marks:" + str(average))

print("Data saved successfully!")
                     
