import random

number_to_guess = 7 
max_attempts = 6 

attempts = 0

print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 10. Try to guess it.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == number_to_guess:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
