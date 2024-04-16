import tkinter as tk
import tkinter.messagebox
import random


# Create a class called GuessingGame
class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")

        # Set the maximum range and attempts to None
        self.max_range = None
        self.max_attempts = None

        # Set the secret number and attempts to None
        self.secret_number = None
        self.attempts = None

        # Create the widgets for the GUI and pack them into the window (master)
        self.rules_label = tk.Label(master, text="")
        self.rules_label.pack()

        # Create a label for the difficulty and pack it into the window (master)
        self.difficulty_label = tk.Label(master, text="Choose difficulty (easy/medium/hard):")
        self.difficulty_label.pack()

        # Create an entry for the difficulty and pack it into the window (master)
        self.difficulty_label = tk.Label(master, text="")
        self.difficulty_label.pack()

        # Create an entry for the difficulty and pack it into the window (master)
        self.diffculty_entry = tk.Entry(master)
        self.diffculty_entry.pack()

        # Create a start button and pack it into the window (master)
        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()

        # Create a play again button and pack it into the window (master)
        self.guess_lable = tk.Label(master, text="Enter you guess:")
        self.guess_lable.pack()

        # Create a play again button and pack it into the window (master)
        self.remaining_attempts_label = tk.Label(master, text="")
        self.remaining_attempts_label.pack()

        # Create an entry for the guess and pack it into the window (master)
        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        # Create a result label and pack it into the window (master)
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        # Create a guess button and pack it into the window (master)
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

    # Define a method to update the difficulty label with the current difficulty
    def update_difficulty(self, difficulty):
        difficulty_text = f"Current Difficulty: {difficulty.capitalize()}"
        self.difficulty_label['text'] = difficulty_text

    # Define a method to display the rules of the game
    def display_rules(self):
        rules_text = f"Rules:\n1. You have {self.max_attempts} attempts to guess the secret number.\n"
        rules_text += f"2. The secret number is between 1 and {self.max_range}.\n"
        rules_text += "3. After each guess, you'll get feedback if your guess is too high or too low."
        self.rules_label['text'] = rules_text

    # Define a method to display the remaining attempts
    def remaining_attempts_attempts(self):
        remaining_attempts_text = f"Remaining attempts: {self.max_attempts - self.attempts}"
        self.remaining_attempts_label['text'] = remaining_attempts_text

    # Define a method to start the game
    def start_game(self):
        difficulty = self.diffculty_entry.get().lower()
        if difficulty == "easy":
            self.max_range = 50
            self.max_attempts = 10

        # Set the maximum range and attempts based on the difficulty
        elif difficulty == "medium":
            self.max_range = 500
            self.max_attempts = 7

        # Set the maximum range and attempts based on the difficulty
        else:  # difficulty == "hard"
            self.max_range = 1000
            self.max_attempts = 5

        # Update the difficulty label with the current difficulty
        self.update_difficulty(difficulty)

        # Generate a random secret number between 1 and the maximum range
        self.secret_number = random.randint(1, self.max_range)
        self.attempts = 0

        # Display the rules and remaining attempts
        self.display_rules()
        self.remaining_attempts_attempts()

        # Reset the text of the result label and guess entry
        self.result_label['text'] = ""
        self.guess_entry.delete(0, 'end')

    # Define a method to ask the user if they want to play again
    def play_again(self):
        play_again = tk.messagebox.askyesno("Play Again?", "Do you want to play again?")
        if play_again:
            self.start_game()
        else:
            self.master.quit()

    # Define a method to check the user's guess
    def check_guess(self):
        self.attempts += 1
        self.remaining_attempts_attempts()

        # Get the user's guess from the guess entry
        guess = int(self.guess_entry.get())

        if guess < self.secret_number:
            self.result_label['text'] = "Too low! Try again."
        elif guess > self.secret_number:
            self.result_label['text'] = "Too high! Try again."
        else:
            self.result_label['text'] = f"Congratulations! You guessed the number in {self.attempts} attempts."

        if self.attempts == self.max_attempts and guess != self.secret_number:
            self.result_label['text'] = f"Sorry, you ran out of attempts. The number was {self.secret_number}."
            self.play_again()


# Create the main window and start the application
root = tk.Tk()
# Create an instance of the GuessingGame class
my_game = GuessingGame(root)
# Start the application
root.mainloop()
