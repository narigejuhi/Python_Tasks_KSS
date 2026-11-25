##5. Employee Management System (OOP + File + Dict) 
##Scenario: 
##Manage employee data. 
##Task: 
##● Create a class Employee 
##● Store employees in a dictionary 
##● Save data to a file 
##● Use exception handling for invalid salary input 
##● Use loop to display all employees


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


employees = {}

try:
    n = int(input("Enter number of employees: "))

    for i in range(n):

        name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))

        if salary < 0:
            raise ValueError("Salary cannot be negative")

        emp = Employee(name, salary)

        employees[name] = emp

    # Save data into file
    with open("employees.txt", "w") as file:

        for name, emp in employees.items():
            file.write(name + " : " + str(emp.salary) + "\n")

    # Display employees
    print("\nEmployee Details:")

    for emp in employees.values():
        emp.display()

except ValueError as e:
    print("Invalid input:", e)

except Exception as e:
    print("Error:", e)
