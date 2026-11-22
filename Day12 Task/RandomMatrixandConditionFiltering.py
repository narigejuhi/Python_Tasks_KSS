##10. Random Matrix and Condition Filtering
##Scenario:
##● Generate a 3×3 matrix of random numbers (0–50).
##Task:
##● Filter elements greater than 25.
##● Print filtered values.

import numpy as np

matrix = np.random.randint(0, 51, (3, 3))

print("Original Matrix:")
print(matrix)

result = matrix[matrix > 25]

print("Filtered Values:")
print(result)
