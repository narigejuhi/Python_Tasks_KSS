##7. Generator-based Log Reader 
##Scenario: 
##A large log file needs to be processed. 
##Task: 
##● Create a generator to read file line by line 
##● Use loop to process logs 
##● Use condition to filter errors 
##● Count occurrences using a dictionary


# Create sample log file
with open("application.log", "w") as file:
    file.write("INFO: Application started\n")
    file.write("ERROR: File not found\n")
    file.write("INFO: User logged in\n")
    file.write("ERROR: Database failed\n")
    file.write("ERROR: Connection lost\n")

# Generator function
def read_logs():

    with open("application.log", "r") as file:

        for line in file:
            yield line.strip()


error_count = {}

# Process logs
for log in read_logs():

    print(log)

    if "ERROR" in log:

        if "ERROR" in error_count:
            error_count["ERROR"] += 1
        else:
            error_count["ERROR"] = 1

print("\nError Count:", error_count)
