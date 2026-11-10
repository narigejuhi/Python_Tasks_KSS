#* List of Dictionaries: Given the following data:
 
##    ```python
##    employees = [
##        {"name": "John", "age": 25, "salary": 30000},
##        {"name": "Alice", "age": 30, "salary": 50000},
##        {"name": "Bob", "age": 28, "salary": 40000},
##        {"name": "David", "age": 35, "salary": 60000}
##    ]
##    ```
 
##    Perform the following:
## * Find the employee with the highest salary.
## * Filter employees whose salary is greater than 35,000.
## * Calculate the average salary.
## * Create a list containing only employee names.


employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]

# 1. Highest salary
highest = max(employees, key=lambda x: x["salary"])
print("Highest salary:", highest)

# 2. Salary greater than 35000
print("Employees earning above 35000:")

for emp in employees:
    if emp["salary"] > 35000:
        print(emp["name"], emp["salary"])

# 3. Average salary
total = 0

for emp in employees:
    total += emp["salary"]

average = total / len(employees)

print("Average salary:", average)

# 4. Employee names
names = []

for emp in employees:
    names.append(emp["name"])

print("Employee names:", names)
