##2. Student Marks Analysis
##Given marks of 5 students in 3 subjects:
##marks = np.array([
##[70, 80, 90],
##[60, 75, 85],
##[50, 65, 70],
##[90, 95, 85],
##[40, 55, 60]
##])
##Task:
##● Calculate total marks of each student.
##● Identify students whose total marks are above the class average.
##


import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])

total = np.sum(marks, axis=1)

average = np.mean(total)

result = total[total > average]

print("Total marks:", total)
print("Class average:", average)
print("Above average:", result)
