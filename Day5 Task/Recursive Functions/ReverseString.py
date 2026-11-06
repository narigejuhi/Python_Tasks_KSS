#4. Write a recursive function to reverse a string.


def reverse_string(s):
    result = ""
    for i in s:
        result = i + result
    return result
print(reverse_string("python"))
