#8. Write a program to check whether a string is a palindrome.

a = input("Enter a string:")
rev = "".join(reversed(a))
if a == rev:
    print("palindrome")
else:
    print("Not a palindrome")
    
              
