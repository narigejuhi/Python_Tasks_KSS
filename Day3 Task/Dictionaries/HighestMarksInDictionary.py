#8. Write a program to find the student with the highest marks from a dictionary.

students = {
    "Juhi": 90,
    "Puja": 85,
    "Vaishu": 65
}

topper = max(students, key=students.get)
print("Topper:", topper)
print("Highest Marks:", students[topper])
