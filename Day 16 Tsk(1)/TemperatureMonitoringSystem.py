##4. Temperature Monitoring System 
##Scenario: 
##temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
##days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
##Task: 
##● Create DataFrame 
##● Plot: 
##○ Line graph → daily temperature trend 
##○ Bar chart → day-wise temperature 
##○ Pie chart → proportion of high (>30) vs low temps 
##○ Histogram → temperature frequency 
##○ Scatter plot → day index vs temperature
##


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df = pd.DataFrame({"Day": days, "Temp": temps})
print(df)

high = (df["Temp"] > 30).sum()
low = (df["Temp"] <= 30).sum()
print("High:", high, "Low:", low)

fig, ax = plt.subplots(2, 3, figsize=(16, 9))

ax[0, 0].plot(df["Day"], df["Temp"], marker="o", color="tomato")
ax[0, 0].set_title("Line: Daily Temperature Trend")
ax[0, 0].set_xlabel("Day"); ax[0, 0].set_ylabel("Temperature"); ax[0, 0].grid(True)

ax[0, 1].bar(df["Day"], df["Temp"], color="steelblue")
ax[0, 1].set_title("Bar: Day-wise Temperature")
ax[0, 1].set_xlabel("Day"); ax[0, 1].set_ylabel("Temperature")

ax[0, 2].pie([high, low], labels=["High (>30)", "Low (<=30)"],
             autopct="%1.1f%%", colors=["#f44336", "#2196f3"], startangle=90)
ax[0, 2].set_title("Pie: High vs Low Temps")

ax[1, 0].hist(df["Temp"], bins=5, color="orchid", edgecolor="black")
ax[1, 0].set_title("Histogram: Temperature Frequency")
ax[1, 0].set_xlabel("Temperature"); ax[1, 0].set_ylabel("Frequency")

ax[1, 1].scatter(df.index, df["Temp"], color="darkorange")
ax[1, 1].set_title("Scatter: Day Index vs Temperature")
ax[1, 1].set_xlabel("Day Index"); ax[1, 1].set_ylabel("Temperature")

ax[1, 2].axis("off")

fig.suptitle("Temperature Monitoring System")
plt.tight_layout()
plt.show()

