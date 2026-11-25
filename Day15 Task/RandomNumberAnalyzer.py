##2. Random Number Analyzer 
##Scenario: 
##A system generates random numbers for testing. 
##Task: 
##● Use random to generate 10 numbers 
##● Store in a list 
##● Use loop + condition to count even/odd numbers 
##● Use set to remove duplicates


import random

numbers = []

#Generate 10 random numbers
for i in range(10):
    num = random.randint(1, 20)
    numbers.append(num)

print("Numbers:", numbers)

even = 0
odd = 0

#Count even and odd numbers

for num in numbers:
    if num % 2 == 0:
        even += 1

    else:

        odd += 1

print("Even Numbers:", even)
print("Odd Numbers:", odd)

#Remove duplicates
unique_numbers = set(numbers)

print("Unique Numbers:", unique_numbers)
