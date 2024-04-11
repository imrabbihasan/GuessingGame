import random


def guess_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again")
        elif guess > secret_number:
            print("Too high!, Try again")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            return
    print(f"Sorry, you ran out of attempts. The number was {secret_number}.")


# Start the game
guess_game()
