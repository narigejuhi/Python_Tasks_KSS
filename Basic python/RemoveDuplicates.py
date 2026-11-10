## 2\. Medium Level.
#1.* Remove Duplicates: Given a list `[1, 2, 3, 2, 4, 1, 5, 3]`, remove duplicate elements while preserving the original order. Do not use `set()`.


numbers = [1, 2, 3, 2, 4, 1, 5, 3]

result = []

for i in numbers:
    if i not in result:
        result.append(i)

print(result)
