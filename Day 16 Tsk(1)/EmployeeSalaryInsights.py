##3. Employee Salary Insights 
##Scenario: 
##salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
##departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 
##Task: 
##● Convert into DataFrame 
##● Plot: 
##○ Line graph → salary trend 
##○ Bar chart → department-wise salary comparison 
##○ Pie chart → department distribution 
##○ Histogram → salary distribution 
##○ Scatter plot → index vs salary 


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df = pd.DataFrame({"Department": departments, "Salary": salaries})
print(df)

dept_avg = df.groupby("Department")["Salary"].mean()     # for bar chart
dept_count = df["Department"].value_counts()             # for pie chart
print(dept_avg)

fig, ax = plt.subplots(2, 3, figsize=(16, 9))

ax[0, 0].plot(df.index, df["Salary"], marker="o")
ax[0, 0].set_title("Line: Salary Trend")
ax[0, 0].set_xlabel("Employee Index"); ax[0, 0].set_ylabel("Salary"); ax[0, 0].grid(True)

ax[0, 1].bar(dept_avg.index, dept_avg.values, color="steelblue")
ax[0, 1].set_title("Bar: Avg Salary by Department")
ax[0, 1].set_xlabel("Department"); ax[0, 1].set_ylabel("Average Salary")

ax[0, 2].pie(dept_count.values, labels=dept_count.index, autopct="%1.1f%%", startangle=90)
ax[0, 2].set_title("Pie: Department Distribution")

ax[1, 0].hist(df["Salary"], bins=5, color="orchid", edgecolor="black")
ax[1, 0].set_title("Histogram: Salary Distribution")
ax[1, 0].set_xlabel("Salary"); ax[1, 0].set_ylabel("Frequency")

ax[1, 1].scatter(df.index, df["Salary"], color="tomato")
ax[1, 1].set_title("Scatter: Index vs Salary")
ax[1, 1].set_xlabel("Index"); ax[1, 1].set_ylabel("Salary")

ax[1, 2].axis("off")

fig.suptitle("Employee Salary Insights")
plt.tight_layout()
plt.show()

