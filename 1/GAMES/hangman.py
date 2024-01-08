import tkinter as tk
import random

# List of words for the game
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Select a random word from the list
selected_word = random.choice(words)
word_length = len(selected_word)

# Initialize the display word with underscores
display_word = ["_"] * word_length

# Initialize variables for the game
attempts = 6  # Number of incorrect attempts allowed

# Create the main window
root = tk.Tk()
root.title("Hangman Game")

# Create a label to display the word
word_label = tk.Label(root, text=" ".join(display_word))
word_label.pack()

# Create a label to display the number of attempts left
attempts_label = tk.Label(root, text=f"Attempts left: {attempts}")
attempts_label.pack()

# Create a function to update the display word
def update_display_word():
    word_label.config(text=" ".join(display_word))

# Create a function to handle user input
def guess_letter():
    global attempts
    letter = entry.get()
    entry.delete(0, tk.END)

    if letter in selected_word:
        for i in range(word_length):
            if selected_word[i] == letter:
                display_word[i] = letter
        update_display_word()
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts left: {attempts}")

        if attempts == 0:
            word_label.config(text=f"Game Over. The word was: {selected_word}")
            entry.config(state="disabled")

    if "_" not in display_word:
        word_label.config(text="You Win!")

# Create an entry widget for letter input
entry = tk.Entry(root)
entry.pack()

# Create a button to guess the letter
guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack()

# Start the game by displaying underscores
update_display_word()

# Start the Tkinter main loop
root.mainloop()
