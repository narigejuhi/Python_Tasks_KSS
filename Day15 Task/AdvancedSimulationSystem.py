##10. Advanced Simulation System 
##Scenario: 
##Simulate exam results and generate reports. 
##Task: 
##● Generate random marks using random 
##● Store in NumPy array 
##● Convert to Pandas DataFrame 
##● Use OOP to represent Student 
##● Use conditions + loops to assign grades 
##● Save report to file 
##● Handle errors using try-except 
##● Use math module for statistics


import random
import numpy as np
import pandas as pd
import math


# Student class
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 60:
            return "C"

        elif self.marks >= 40:
            return "D"

        else:
            return "Fail"


try:

    names = ["Juhi", "Ravi", "Priya", "Anu", "Vijay"]

    # Generate random marks
    marks = np.array([
        random.randint(0, 100) for i in range(5)
    ])

    students = []

    # Create student objects
    for i in range(len(names)):

        student = Student(names[i], int(marks[i]))

        students.append(student)

    # Assign grades
    results = []

    for student in students:

        grade = student.calculate_grade()

        results.append({
            "Name": student.name,
            "Marks": student.marks,
            "Grade": grade
        })

    # Create DataFrame
    df = pd.DataFrame(results)

    print("Exam Results:")
    print(df)

    # Statistics
    average = math.floor(np.mean(marks))

    print("\nAverage Marks:", average)
    print("Highest Marks:", np.max(marks))
    print("Lowest Marks:", np.min(marks))

    # Save report
    df.to_csv("exam_report.csv", index=False)

    print("\nReport saved successfully!")

except ValueError as e:
    print("Invalid value:", e)

except Exception as e:
    print("Error:", e)
