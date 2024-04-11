# Number Guessing Game

The Number Guessing Game is a simple yet enjoyable Python project for beginners. It's a classic game where the computer generates a random number, and the player has to guess the number within a limited number of attempts.

## How to Play

1. The game will display a header and the rules.
2. You have 10 attempts to guess the secret number, which is between 1 and 100.
3. After each guess, you'll receive feedback indicating whether your guess was too high or too low.
4. If you guess the correct number within the allotted attempts, you win! The game will display a congratulatory message along with the number of attempts it took you.
5. If you run out of attempts, the game will reveal the secret number, and you can choose to play again.

## Features

- Interactive gameplay with user input validation
- Visually appealing header and clear instructions
- Option to play again after each game

## Requirements

- Python 3.x

## How to Run

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the following command: python GuessingGame.py

## Code Overview

The `guessing_game.py` file contains the following functions:

- `display_header()`: Prints a visually appealing header for the game.
- `display_rules(max_attempts)`: Prints the game rules, taking the maximum number of attempts as an argument.
- `get_user_guess()`: Handles user input validation to ensure the user enters a valid number between 1 and 100.
- `play_game()`: Contains the main game logic and handles user interactions.

The `play_game()` function is called at the end of the script to start the game.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
