#Create a Python module named calculator.py that contains functions to perform: 
##● Addition 
##● Subtraction 
##● Multiplication 
##● Division 
##Then write another Python program that imports this module and performs calculations 
##based on user input. 


#Addition
def add(a,b):
    return a +b
#Subtraction
def sub(a,b):
    return a - b
#Multipliction
def mul(a,b):
    return a * b
#Division
def div(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
