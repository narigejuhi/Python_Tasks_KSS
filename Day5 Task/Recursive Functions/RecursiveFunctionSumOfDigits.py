#3. Write a recursive function to calculate the sum of digits of a number.
#Example: Input = 123 → Output = 6


def sum_digits(n):
    total = 0

    for i in str(n):
        total = total + int(i)
    return total
print(sum_digits(123))
