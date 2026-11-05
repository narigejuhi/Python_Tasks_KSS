#5. Write a program to check whether a substring exists in a string.

a = input("Enter a string:")
count = 0
for i in a:
    if i.lower() in "aeiou":
        count += 1
print("Number of vowels:",count)
