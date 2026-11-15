#6. Employee Salary Management System 
##A company stores employee data in a file employees.txt in the format: 
##EmployeeName Salary 
##Example: 
##Ramesh 25000 
##Sita 30000 
##Arun 28000 
##Write a Python program that: 
##● Reads employee data from the file 
##● Displays all employee details 
##● Finds the employee with the highest salary 
##● Appends a new employee record to the file. 


# Read employee details
f = open("employees.txt", "r")

employees = []

for line in f:
    name, salary = line.split()
    employees.append((name, int(salary)))

f.close()

# Display employee details
print("Employee Details:")

for name, salary in employees:
    print(name, salary)

# Find highest salary
highest = max(employees, key=lambda x: x[1])

print("Highest Salary Employee:")
print(highest[0], highest[1])

# Add new employee
f = open("employees.txt", "a")

name = input("Enter employee name: ")
salary = int(input("Enter employee salary: "))

f.write(name + " " + str(salary) + "\n")

f.close()

print("New employee added successfully!")
