#5.  Create a Number Guessing Game where: 
##● The program generates a random number between 1 and 50 using random. 
##● The user has 5 attempts to guess the number. 



import random
number = random.randint(1,50)

print("Welcome to number Guessing Game!")
print("Guess a number between 1 and 50")
print("You have 5 attempts")
for i in range(5):
     guess = int(input("Enter your guess:"))
     if guess == number:
        print("Congratulations! You guessed correctly.")
        break
     
     elif guess < number:
        print("Too low! Try again.")
     else:
        print("Too high! Try again.")

else:
    print("Game over!")
    print("Correct number is:",number)
    
