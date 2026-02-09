import random

print("=== Guess the Number Game ===")
print("I'm thinking of a number between 1 and 100")

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You got it in {attempts} attempts!")
        break
else:
    print(f"Game over! The number was {secret_number}")
