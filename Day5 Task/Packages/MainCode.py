#Write a Python program that imports the package and uses functions from both modules.

from Utilities.MathOperations import *
from Utilities.StringOperations import *

#User Input
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print(add(a,b))
print(mul(a,b))

Text = str(input("Enter text:"))
print(uppercase(Text))
print(count_characters(Text))
