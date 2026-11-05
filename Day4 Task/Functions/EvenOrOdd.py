#15. Write a function to check whether a number is even or odd.

def check(n):
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
a = int(input("Enter a number:"))
check(a)
