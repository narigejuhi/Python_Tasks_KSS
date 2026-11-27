##9. Combined Visualization Dashboard 
##Scenario: 
##sales = np.array([100, 200, 150, 300]) 
##products = ["A", "B", "C", "D"] 
##Task: 
##● Create DataFrame 
##● Plot: 
##○ Line graph (trend) 
##○ Bar chart (comparison) 
##○ Pie chart (distribution) 
##● Show all in single figure (subplots)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

df = pd.DataFrame({"Product": products, "Sales": sales})
print(df)

fig, ax = plt.subplots(1, 3, figsize=(15, 4.5))

ax[0].plot(df["Product"], df["Sales"], marker="o")
ax[0].set_title("Trend")
ax[0].set_xlabel("Product")
ax[0].set_ylabel("Sales")
ax[0].grid(True)

ax[1].bar(df["Product"], df["Sales"], color="steelblue")
ax[1].set_title("Comparison")
ax[1].set_xlabel("Product")
ax[1].set_ylabel("Sales")

ax[2].pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%", startangle=90)
ax[2].set_title("Distribution")

fig.suptitle("Sales Dashboard")
plt.tight_layout()
plt.show()

