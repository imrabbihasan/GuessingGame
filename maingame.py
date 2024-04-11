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


def display_rules(max_attempts):
    print("\nRules:")
    print(f"1. You have {max_attempts} attempts to guess the secret number.")
    print("2. The secret number is between 1 and 100.")
    print("3. After each guess, you'll get feedback if your guess is to high or too low.")


def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Invalid input! Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def play_game():
    # clear_console()
    display_header()
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    display_rules(max_attempts)

    while attempts < max_attempts:
        guess = get_user_guess()
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
