#1. Student Attendance Record 
##A teacher wants to store student attendance in a file named attendance.txt. Write a 
##Python program that takes a student name as input and appends it to the file. Then 
##display the contents of the file.


#Open file in append mode
f = open("attendance.txt","a")

name = input("Enter student name:")
f.write(name + "\n")
f.close()

#Read and display file

f = open("attendance.txt","r")

print("Attendance Records:")
print(f.read())

f.close()

