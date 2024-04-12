import tkinter as tk
import tkinter.messagebox
import random


class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")

        self.max_range = None
        self.max_attempts = None

        self.secret_number = None
        self.attempts = None

        self.rules_label = tk.Label(master, text="")
        self.rules_label.pack()

        self.difficulty_label = tk.Label(master, text="Choose difficulty (easy/medium/hard):")
        self.difficulty_label.pack()

        self.difficulty_label = tk.Label(master, text="")
        self.difficulty_label.pack()

        self.diffculty_entry = tk.Entry(master)
        self.diffculty_entry.pack()

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.guess_lable = tk.Label(master, text="Enter you guess:")
        self.guess_lable.pack()

        self.remaining_attempts_label = tk.Label(master, text="")
        self.remaining_attempts_label.pack()

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

    def update_difficulty(self, difficulty):
        difficulty_text = f"Current Difficulty: {difficulty.capitalize()}"
        self.difficulty_label['text'] = difficulty_text

    def display_rules(self):
        rules_text = f"Rules:\n1. You have {self.max_attempts} attempts to guess the secret number.\n"
        rules_text += f"2. The secret number is between 1 and {self.max_range}.\n"
        rules_text += "3. After each guess, you'll get feedback if your guess is too high or too low."
        self.rules_label['text'] = rules_text

    def remaining_attempts_attempts(self):
        remaining_attempts_text = f"Remaining attempts: {self.max_attempts - self.attempts}"
        self.remaining_attempts_label['text'] = remaining_attempts_text

    def start_game(self):
        difficulty = self.diffculty_entry.get().lower()
        if difficulty == "easy":
            self.max_range = 50
            self.max_attempts = 10

        elif difficulty == "medium":
            self.max_range = 500
            self.max_attempts = 7

        else:  # difficulty == "hard"
            self.max_range = 1000
            self.max_attempts = 5

        self.update_difficulty(difficulty)

        self.secret_number = random.randint(1, self.max_range)
        self.attempts = 0

        self.display_rules()
        self.remaining_attempts_attempts()

        # Reset the text of the result label and guess entry
        self.result_label['text'] = ""
        self.guess_entry.delete(0, 'end')

    def play_again(self):
        play_again = tk.messagebox.askyesno("Play Again?", "Do you want to play again?")
        if play_again:
            self.start_game()
        else:
            self.master.quit()

    def check_guess(self):
        self.attempts += 1
        self.remaining_attempts_attempts()

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


root = tk.Tk()
my_game = GuessingGame(root)
root.mainloop()
