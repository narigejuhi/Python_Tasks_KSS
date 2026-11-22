##3. Employee Data Copy Issue (Shallow vs Deep Copy)
##A company stores employee data:
##employees = [[101, "A"], [102, "B"], [103, "C"]]
##Scenario:
##● Create a shallow copy of the list.
##● Modify one nested list (e.g., change "A" to "Z").
##● Observe changes in both lists.
##Task:
##● Explain why the change reflects in both.
##● Fix it using deep copy.


import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]

# Shallow copy
shallow = copy.copy(employees)

employees[0][1] = "Z"

print("Original:", employees)
print("Shallow Copy:", shallow)

# Deep copy
deep = copy.deepcopy(employees)

employees[0][1] = "X"

print("Original:", employees)
print("Deep Copy:", deep)
