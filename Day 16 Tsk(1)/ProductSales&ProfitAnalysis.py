##5. Product Sales & Profit Analysis 
##Scenario: 
##sales = np.array([200, 300, 250, 400, 350]) 
##profit = np.array([50, 70, 60, 90, 80]) 
##products = ["A", "B", "C", "D", "E"] 
##Task: 
##● Create DataFrame 
##● Plot: 
##○ Line graph → sales trend 
##○ Bar chart → product vs sales 
##○ Pie chart → sales contribution 
##○ Histogram → profit distribution 
##○ Scatter plot → sales vs profit


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({"Product": products, "Sales": sales, "Profit": profit})
print(df)

fig, ax = plt.subplots(2, 3, figsize=(16, 9))

ax[0, 0].plot(df["Product"], df["Sales"], marker="o")
ax[0, 0].set_title("Line: Sales Trend")
ax[0, 0].set_xlabel("Product"); ax[0, 0].set_ylabel("Sales"); ax[0, 0].grid(True)

ax[0, 1].bar(df["Product"], df["Sales"], color="steelblue")
ax[0, 1].set_title("Bar: Product vs Sales")
ax[0, 1].set_xlabel("Product"); ax[0, 1].set_ylabel("Sales")

ax[0, 2].pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%", startangle=90)
ax[0, 2].set_title("Pie: Sales Contribution")

ax[1, 0].hist(df["Profit"], bins=5, color="orchid", edgecolor="black")
ax[1, 0].set_title("Histogram: Profit Distribution")
ax[1, 0].set_xlabel("Profit"); ax[1, 0].set_ylabel("Frequency")

ax[1, 1].scatter(df["Sales"], df["Profit"], color="tomato")
ax[1, 1].set_title("Scatter: Sales vs Profit")
ax[1, 1].set_xlabel("Sales"); ax[1, 1].set_ylabel("Profit")

ax[1, 2].axis("off")

fig.suptitle("Product Sales & Profit Analysis")
plt.tight_layout()
plt.show()
