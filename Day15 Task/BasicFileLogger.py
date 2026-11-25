##4. Basic File Logger 
##Scenario: 
##A system logs user actions. 
##Task: 
##● Take user input 
##● Store logs in a file 
##● Use loop to allow multiple entries 
##● Handle file errors using exception handling


try:
    with open("logs.txt", "a") as file:

        while True:
            action = input("Enter user action (stop to exit):")

            if action.lower() == "stop":
                break
            file.write(action + "\n")

    print("Logs saved successfully!")

except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("permission denied!")
except Exception as e:
    print("Error:", e)
    
