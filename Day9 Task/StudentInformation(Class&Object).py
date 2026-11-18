#1. Student Information System (Class & Object) 
##A school wants a program to store student details. Create a Student class with 
##attributes such as name, roll number, and marks. Create objects for at least three 
##students and display their details.


class Student():
    name="Juhi"
    roll_number=9
    marks=78
    def display(self):
        print("Student name is:",self.name)
        print("Student roll number:",self.roll_number)
        print("Students marks:",self.marks)
obj=Student()
obj.display()
obj1=Student()
obj1.name="Ravi"
obj1.roll_number=11
obj1.marks=78
obj1.display()
obj2=Student()
obj2.name="Priya"
obj2.roll_number=12
obj2.marks=69
obj2.display()
