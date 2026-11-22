##11. Boolean Masking for Salary Analysis
##Scenario:
##Employee salaries:
##[25000, 40000, 15000, 50000, 30000]
##Task:
##● Filter salaries above 30000.
##● Count how many employees satisfy this condition.


import numpy as np

salary = np.array([25000, 40000, 15000, 50000, 30000])

result = salary[salary > 30000]

print("Salaries Above 30000:", result)

count = np.count_nonzero(salary > 30000)

print("Number of Employees:", count)
