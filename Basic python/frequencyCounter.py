#2.* Frequency Counter: Given a string `"programming"`, create a dictionary that counts how many times each character appears.
#Expected output:
 #```python
    #{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1,
    # 'm': 2, 'i': 1, 'n': 1}
    #```


s = "programming"

frequency = {}

for i in s:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)
