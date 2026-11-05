#17. Write a program using the built-in max() function to find the largest number in a list.

a = [10,50,30,80,20]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)
