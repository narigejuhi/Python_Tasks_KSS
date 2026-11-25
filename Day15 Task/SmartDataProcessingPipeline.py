##9. Smart Data Processing Pipeline 
##Scenario: 
##A system processes numeric data from file. 
##Task: 
##● Read numbers from a file 
##● Use NumPy for calculations (mean, std) 
##● Convert results to Pandas DataFrame 
##● Use exception handling for bad data 
##● Use a generator to stream data 
##● Apply decorator to measure execution time


import numpy as np
import pandas as pd
import time

# Create data file
with open("numbers.txt", "w") as file:
    file.write("10\n20\n30\n40\n50\nabc\n")


# Generator to read numbers
def read_numbers():

    with open("numbers.txt", "r") as file:

        for line in file:
            yield line.strip()


# Decorator to calculate execution time
def execution_time(func):

    def wrapper():

        start = time.time()

        result = func()

        end = time.time()

        print("Execution Time:", end - start)

        return result

    return wrapper


@execution_time
def process_data():

    numbers = []

    for value in read_numbers():

        try:
            numbers.append(float(value))

        except ValueError:
            print("Invalid data:", value)

    # NumPy calculations
    arr = np.array(numbers)

    mean = np.mean(arr)
    std = np.std(arr)

    # Pandas DataFrame
    df = pd.DataFrame({
        "Numbers": arr
    })

    print("\nDataFrame:")
    print(df)

    print("\nMean:", mean)
    print("Standard Deviation:", std)


process_data()
