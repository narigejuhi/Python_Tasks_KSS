#5. Word Counter Program 
##A writer saves an article in a file called article.txt. Write a Python program that: 
##● Opens and reads the file 
##● Counts the number of words, lines, and characters in the file 
##● Displays the results.


f = open("article.txt", "r")

#read()-Reads the complete file
data = f.read()

#split()-Separates words
words = data.split()
#splitlines()-separates lines
lines = data.splitlines()

#len()-Counts the number of items or characters
characters = len(data)

print("Number of words:", len(words))
print("Number of lines:", len(lines))
print("Number of characters:", characters)

f.close()
