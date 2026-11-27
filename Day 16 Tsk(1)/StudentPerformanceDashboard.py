##1. Student Performance Dashboard
##Scenario:
##A school records marks of students in one subject:
##marks = np.array([45, 67, 89, 56, 72, 91, 38])
##students = ["A", "B", "C", "D", "E", "F", "G"]
##Task:
##● Convert to Pandas DataFrame
##● Plot:
##○ Line graph → trend of marks
##○ Bar chart → student vs marks
##○ Pie chart → Pass (>50) vs Fail
##○ Histogram → distribution of marks
##○ Scatter plot → index vs marks


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({"Student": students, "Marks": marks})
print(df)

passed = (df["Marks"] > 50).sum()
failed = (df["Marks"] <= 50).sum()

fig, ax = plt.subplots(2, 3, figsize=(16, 9))

ax[0, 0].plot(df["Student"], df["Marks"], marker="o")
ax[0, 0].set_title("Line: Trend of Marks")
ax[0, 0].set_xlabel("Student"); ax[0, 0].set_ylabel("Marks"); ax[0, 0].grid(True)

ax[0, 1].bar(df["Student"], df["Marks"], color="steelblue")
ax[0, 1].set_title("Bar: Student vs Marks")
ax[0, 1].set_xlabel("Student"); ax[0, 1].set_ylabel("Marks")

ax[0, 2].pie([passed, failed], labels=["Pass (>50)", "Fail"],
             autopct="%1.1f%%", colors=["#4caf50", "#f44336"], startangle=90)
ax[0, 2].set_title("Pie: Pass vs Fail")

ax[1, 0].hist(df["Marks"], bins=5, color="orchid", edgecolor="black")
ax[1, 0].set_title("Histogram: Distribution of Marks")
ax[1, 0].set_xlabel("Marks"); ax[1, 0].set_ylabel("Frequency")

ax[1, 1].scatter(df.index, df["Marks"], color="tomato")
ax[1, 1].set_title("Scatter: Index vs Marks")
ax[1, 1].set_xlabel("Index"); ax[1, 1].set_ylabel("Marks")

ax[1, 2].axis("off")

fig.suptitle("Student Performance Dashboard")
plt.tight_layout()
plt.show()
