##10. Data Cleaning + Visualization 
##Scenario: 
##data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
##Task: 
##1. Convert to Pandas Series 
##2. Replace NaN with mean 
##3. Plot: 
##○ Line graph of cleaned data 
##○ Bar chart of values > average


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

# 1. Convert to Series
s = pd.Series(data)

# 2. Replace NaN with mean (mean ignores NaN -> 187.5)
mean_val = s.mean()
clean = s.fillna(mean_val)
print("Mean:", mean_val)
print(clean)

# 3. Plots
fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))

ax[0].plot(clean.index, clean.values, marker="o")
ax[0].set_title("Cleaned Data")
ax[0].set_xlabel("Index")
ax[0].set_ylabel("Value")
ax[0].grid(True)

above = clean[clean > clean.mean()]
ax[1].bar(above.index.astype(str), above.values, color="darkorange")
ax[1].set_title(f"Values > Average ({clean.mean():.1f})")
ax[1].set_xlabel("Index")
ax[1].set_ylabel("Value")

plt.tight_layout()
plt.show()

