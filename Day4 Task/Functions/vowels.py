#19. Write a function that takes a string as input and returns the number of vowels.

def vowels(s):
    count = 0
    for i in "aeiou":
        count += s.lower().count(i)
    return count
a = input("Enter a string:")
print(vowels(a))
