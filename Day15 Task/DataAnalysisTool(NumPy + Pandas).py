##6. Data Analysis Tool (NumPy + Pandas) 
##Scenario: 
##Analyze student marks. 
##Task: 
##● Generate marks using NumPy 
##● Convert into Pandas DataFrame 
##● Use conditions to filter passing students 
##● Calculate mean using math/NumPy 
##● Use loop to print results


import numpy as np
import pandas as pd

# Generate marks
marks = np.random.randint(30, 101, 5)

# Create DataFrame
df = pd.DataFrame({
    "Student": ["Juhi", "Ravi", "Priya", "Anu", "Vijay"],
    "Marks": marks
})

print("Student Details:")
print(df)

# Filter passing students
passing = df[df["Marks"] >= 40]

print("\nPassing Students:")
print(passing)

# Calculate mean
average = np.mean(marks)

print("\nAverage Marks:", average)

# Print results using loop
print("\nStudent Results:")

for index, row in df.iterrows():

    if row["Marks"] >= 40:
        print(row["Student"], "Pass")
    else:
        print(row["Student"], "Fail")
