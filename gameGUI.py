import tkinter as tk
import tkinter.messagebox
import random


# Create a class called GuessingGame
class GuessingGame:
    def __init__(self, master):
        self.guess_entry = None
        self.master = master
        self.master.title("Guessing Game")

        # Set the maximum range and attempts to None
        self.max_range = None
        self.max_attempts = None

        # Set the secret number and attempts to None
        self.secret_number = None
        self.attempts = None

        # Initialize the player's score
        self.score = 0

        # Create a label to display to the player's score
        self.score_label = tk.Label(master, text=f"Score: {self.score}", anchor='center', justify='center', bg='light blue')
        self.score_label.pack()

        # Create the widgets for the GUI and pack them into the window (master)
        self.rules_label = tk.Label(master, text="", anchor='center', justify='center', bg='light blue')
        self.rules_label.pack()

        # Create a label for the difficulty and pack it into the window (master)
        self.difficulty_label = tk.Label(master, text="Choose difficulty (easy/medium/hard):", anchor='center',
                                         justify='center', bg='light blue')
        self.difficulty_label.pack()

        # Create an entry for the difficulty and pack it into the window (master)
        self.difficulty_label = tk.Label(master, text="", anchor='center', justify='center', bg='light blue')
        self.difficulty_label.pack()

        # Create an entry for the difficulty and pack it into the window (master)
        self.diffculty_entry = tk.Entry(master)
        self.diffculty_entry.pack()

        # Create a start button and pack it into the window (master)
        self.start_button = tk.Button(master, text="Start Game", command=self.start_game, bg='light pink', fg='black')
        self.start_button.pack()

        # Bind the Enter key to the start_game method
        self.diffculty_entry.bind("<Return>", self.start_game)

        # Create a play again button and pack it into the window (master)
        self.guess_lable = tk.Label(master, text="Enter you guess:", anchor='center', justify='center', bg='light blue')
        self.guess_lable.pack()

        # Bind the Enter key to the check_guess method
        # self.guess_entry.bind("<Return>", self.check_guess)

        # Create a play again button and pack it into the window (master)
        self.remaining_attempts_label = tk.Label(master, text="", anchor='center', justify='center', bg='light blue')
        self.remaining_attempts_label.pack()

        # Create an entry for the guess and pack it into the window (master)
        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        # Create a result label and pack it into the window (master)
        self.result_label = tk.Label(master, text="", anchor='center', justify='center', bg='light blue')
        self.result_label.pack()

        # Create an icon for the Guess button
        self.guess_icon = tk.PhotoImage(file="guess_icon.png", )

        # Resize the icon
        self.guess_icon = self.guess_icon.subsample(2, 2)

        # Create a guess button and pack it into the window (master)
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess, image=self.guess_icon,
                                      compound='left', bg='green', fg='black')
        self.guess_button.pack()

        # Create an icon for the Play Again
        self.play_again_button_icon = tk.PhotoImage(file="play_again.png")

        # Resize the icon
        self.play_again_button_icon = self.play_again_button_icon.subsample(3, 3)

        # Create a play again button
        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again,
                                           image=self.play_again_button_icon, compound='left', bg='red', fg='red')
        self.play_again_button.pack()

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
    def start_game(self, event=None):
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
    def check_guess(self, event=None):
        # Get the user's guess from the guess entry
        guess = self.guess_entry.get()

        # Check if the user has entered a guess
        if not guess:
            self.result_label['text'] = "Please enter a guess."
            return

        self.attempts += 1
        self.remaining_attempts_attempts()

        # Get the user's guess from the guess entry
        guess = int(guess)

        if guess < self.secret_number:
            self.result_label['text'] = "Too low! Try again."
        elif guess > self.secret_number:
            self.result_label['text'] = "Too high! Try again."
        else:
            self.result_label['text'] = f"Congratulations! You guessed the number in {self.attempts} attempts."

            # Update the player's score
            self.score += 1
            # Update the score label
            self.score_label['text'] = f"Score: {self.score}"

        if self.attempts == self.max_attempts and guess != self.secret_number:
            self.result_label['text'] = f"Sorry, you ran out of attempts. The number was {self.secret_number}."
            # self.play_again()
            tk.messagebox.showinfo("Game Over", "Game Over")
            self.start_game()

        # Clear the guess entry
        self.guess_entry.delete(0, 'end')


# Create the main window and start the application
root = tk.Tk()
# Set the size to 500x500 pixels (width x height) using the geometry method of the root window object (root)
root.geometry("500x400")
# Create an instance of the GuessingGame class
my_game = GuessingGame(root)

# Set the Background color of the window
root.configure(bg='light blue')
# Start the application
root.mainloop()
