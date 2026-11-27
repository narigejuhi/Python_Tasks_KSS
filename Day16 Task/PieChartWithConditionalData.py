##8. Pie Chart with Conditional Data 
##Scenario: 
##scores = np.array([40, 60, 80, 30, 90]) 
##Task: 
##● Categorize into: 
##○ Pass (>50) 
##○ Fail (<=50) 
##● Count using NumPy/Pandas 
##● Plot pie chart for Pass vs Fail


import numpy as np
import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

pass_count = np.sum(scores > 50)
fail_count = np.sum(scores <= 50)
print("Pass:", pass_count, "Fail:", fail_count)

plt.pie([pass_count, fail_count], labels=["Pass", "Fail"],
        autopct="%1.1f%%", colors=["#4caf50", "#f44336"], startangle=90)
plt.title("Pass vs Fail")
plt.show()
