#Question: 
##Write a program to check whether a number is a Palindrome. 
##Definition: 
##A number is a Palindrome if it reads the same forward and backward. 
##Example: 
##Number = 121 
##Reverse = 121 
##Output: 
##121 is a Palindrome number


num = int(input("Enter a number:"))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if reverse == num:
    print(num,"is a Palindrom number")
else:
    print(num,"is not a Palindrome number")
    
