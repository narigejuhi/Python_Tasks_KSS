#9. Write a program to count the frequency of each character in a string.

a = input("Enter a string:")
for i in set(a):
    print(i,":",a.count(i))
