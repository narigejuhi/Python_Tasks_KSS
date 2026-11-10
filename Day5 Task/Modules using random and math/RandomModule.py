#1. Write a Python program using the random module to generate 10 random integers between 1 and 100 and store them in a list. Print the list.


import random
a=[]
for i in range(10):
    i=random.randint(1,100)
    a.append(i)
print(a)
