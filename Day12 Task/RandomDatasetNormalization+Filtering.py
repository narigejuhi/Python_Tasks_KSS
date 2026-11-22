##12. Random Dataset Normalization + Filtering
##Scenario:
##● Generate 8 random float values between 0 and 1.
##Task:
##1. Normalize by multiplying with 100
##2. Filter values greater than 50
##3. Sort the filtered values


import numpy as np

# Generate 8 random float values
data = np.random.rand(8)

print("Original Data:", data)

# Normalize by multiplying by 100
normalized = data * 100

print("Normalized Data:", normalized)

# Filter values greater than 50
filtered = normalized[normalized > 50]

# Sort the filtered values
sorted_data = np.sort(filtered)

print("Filtered Values:", filtered)
print("Sorted Values:", sorted_data)
