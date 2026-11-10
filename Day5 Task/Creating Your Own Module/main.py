
#Then write another Python program that imports this module and performs calculations based on user input.

import Calculator

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

print("Addition:",Calculator.add(a,b))
print("Subtraction:",Calculator.sub(a,b))
print("Multiplication:",Calculator.mul(a,b))
print("Division:",Calculator.div(a,b))


#we can use like this from calculator import * instesd of import calculator

from Calculator import *
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
