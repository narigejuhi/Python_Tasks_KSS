#Question: 
##Write a program to check whether a given number is a Strong number. 
##Definition: 
##A Strong number is a number whose sum of factorial of digits is equal to the number itself. 
##Example: 
##Number = 145 
##Calculation: 
##1! + 4! + 5! 
##= 1 + 24 + 120 
##= 145


num = int(input("Enter a number:"))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    fact = 1

    for i in range(1,digit + 1):
        fact = fact * i

    total = total + fact
    temp = temp // 10
if total == num:
    print(num,"is a strong number")
else:
    print(num,"is not a strong number")
    
