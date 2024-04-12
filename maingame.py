import platform
import random
import os


# def clear_console():
#     operating_system = platform.system()
#     if operating_system == "Windows":
#         os.system("cls")
#     elif operating_system == "Linux" or operating_system == "Darwin":
#         os.system("clear")
#     else:
#         print("\n * 100")  # Print 100 newlines for systems where clearing the console is not supported.


def display_header():
    print("╔═══════════════════════════════════════╗")
    print("║        Number Guessing Game           ║")
    print("╚═══════════════════════════════════════╝")


def display_rules(max_attempts, max_range):
    print("\nRules:")
    print(f"1. You have {max_attempts} attempts to guess the secret number.")
    print(f"2. The secret number is between 1 and {max_range}.")
    print("3. After each guess, you'll get feedback if your guess is to high or too low.")


def get_user_guess(max_range):
    while True:
        guess = input(f"Enter your guess (1-{max_range}) or 'quit' to exit: ")
        if guess.lower() == 'quit':
            return None
        try:
            guess = int(guess)
            if 1 <= guess <= max_range:
                return guess
            else:
                print(f"Invalid input! Please enter a number between 1 and {max_range}.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def play_game():
    print("Welcome to the game! You can quit at any time by typing 'quit'.")
    # clear_console()
    display_header()
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty level! Please choose either 'easy', 'medium', or 'hard'.")
        display_header()
        difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    if difficulty == "easy":
        max_range = 50
        max_attempts = 10
    elif difficulty == "medium":
        max_range = 500
        max_attempts = 7
    else: # difficulty == "hard"
        max_range = 100
        max_attempts = 5
    secret_number = random.randint(1, max_range)
    attempts = 0
    display_rules(max_attempts, max_range)

    while attempts < max_attempts:
        guess = get_user_guess(max_range)
        if guess is None:
            print("You chose to quit the game. Welcome to play again!")
            return
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again")
        elif guess > secret_number:
            print("Too high! Try again")
        else:
            print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts.")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again == 'y':
                play_game()
            else:
                print("Thanks for playing")
                return

    print(f"\nSorry, you ran out of attempts. The number was {secret_number}.")
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        open("Thanks for playing!")


play_game()
