##17. Employee Bonus Calculator (Decorators & OOP) 
##A company wants to apply a bonus calculation automatically before displaying the 
##salary. Create an Employee class and use a decorator that modifies the salary by 
##adding a bonus before displaying it.


def bonus(func):
    def wrapper(self):
        salary = func(self)
        return salary + 5000

    return wrapper


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus
    def get_salary(self):
        return self.salary

    def display(self):
        print("Name:", self.name)
        print("Salary with Bonus:", self.get_salary())


e = Employee("Juhi", 30000)
e.display()
