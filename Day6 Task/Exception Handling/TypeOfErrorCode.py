###Q1: Develop a Python program to manage student marks for three subjects. Store the subject
##names in a tuple, maintain unique student names in a set, and store each student’s marks
##in a list inside a dictionary where the key is the student name. Create user-defined
##functions to add a student with marks, display all student records, and calculate the average
##marks of a student. Implement a recursive function to calculate the total marks from the list of
##marks. The program should interact with the user through a simple menu. Also include
##exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError
##(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a
##student name entered does not exist in the dictionary).


subjects = ("Math","Science","English")

students = set()
student_marks = {}

# Recusive function to calculate total
def calculate_total(marks):
    if len(marks) == 0:
        return 0
    return marks[0] + calculate_total(marks[1:])
# Function to add student
def add_student():
    try:
        name = input("Enter student name:")
        if name in students:
            print("student already exists!")
            return
        marks = []
        for subject in subjects:
            mark = int(input("Enter marks for " + subject + ": "))
            marks.append(mark)
            
        students.add(name)
        student_marks[name] = marks
        
            
        print("student added successfully!")
    except ValueError:
        print("Invalid input! Please enter numeric marks.")    
    except TypeError:
        print("Marks data type error.")

#Function to display students
def display_students():
    if len(student_marks) == 0:
        print("No student records found.")
    else:
        for name, marks in student_marks.items():
            print(name,":",marks)
#Function to calculate average
def calculate_average():
    try:
        name = input("Enter student name to calculate average:")
        if name not in student_marks:
            raise NameError
        marks = student_marks[name]
        totle = calculate_total(marks)
        average = totle / len(marks)

        print("Total Marks:",total)
        print("Average Marks:",average)
    except NameError:
        print("Student name not found.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Marks data type error.")

# Main menu
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()

        elif choice == 3:
            calculate_average()

        elif choice == 4:
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")
