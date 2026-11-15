##3. Grocery List Manager 
##A user wants to save grocery items in a file grocery.txt. Write a Python program that 
##takes multiple items from the user and writes them into the file, with each item on a 
##new line.


f = open("grocery.txt", "w")

n = int(input("How many items do you want to enter? "))

for i in range(n):
    item = input("Enter grocery item: ")
    f.write(item + "\n")

f.close()

print("Grocery items saved successfully!")
