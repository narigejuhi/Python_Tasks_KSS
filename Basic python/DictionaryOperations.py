#5.* Dictionary Operations: Create a dictionary containing student names and marks. Add a new student, update an existing student's marks, and print all student details.


students = {
    "Puja": 85,
    "Gouri": 90,
    "Vaishu": 80
}

# Add new student
students["Juhi"] = 95

# Update existing marks
students["Puja"] = 90

# Print all details
for name, marks in students.items():
    print(name, marks)
