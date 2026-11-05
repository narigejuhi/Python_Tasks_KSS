#10. Write a program to remove duplicate characters from a string.

a = input("Enter a string:")
result = ""
for i in a:
    if i not in result:
        result += i
print(result)
