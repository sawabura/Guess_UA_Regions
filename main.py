import turtle
from operations import Operations
from tkinter import messagebox

# GLOBAL CONSTANTS
DIR_IMG = "./blank_ukraine.gif"
TOTAL_TRIES = 26  # Maximum number of tries
SCORE = 0
tries_left = TOTAL_TRIES
title_text = "Guess the region"
prompt_text = "Enter a region name"

# screen setup
screen = turtle.Screen()
screen.setup(width=1000, height=710)
screen.title("UKRAINE REGIONS GAME")
screen.addshape(DIR_IMG)
turtle.shape(DIR_IMG)

# USING BLUEPRINT CLASS
operations = Operations()
print(operations.list_name_regions)
print(operations.data)

while tries_left > 0 and len(operations.guessed_regions) < operations.regions_len:
    # EXCEPTION IF YOU GUESSED AT LEAST 1 REGION - CHANGE TITLE AND PROMPT
    if len(operations.guessed_regions) != 0:
        title_text = f"{SCORE}/{operations.regions_len} correct. Tries: {tries_left}"
        prompt_text = "Enter region name:"

    # GET GUESS WITH FIRST CAPITAL LETTER USING title()
    guess = screen.textinput(title=title_text, prompt=prompt_text).title()

    if guess == "Exit":
        # Check missed regions and save to CSV
        operations.exit_and_save()
        break

    if guess in operations.list_name_regions and guess not in operations.guessed_regions:
        # Correct guess
        SCORE += 1
        operations.add_label(guess)
    else:
        # Wrong guess
        print(f"Wrong guess: {guess}")
    
    # Decrease tries left after each guess
    tries_left -= 1

# Final message
if tries_left == 0:
    final_message = f"Game over! You scored {SCORE} out of {TOTAL_TRIES}."
else:
    final_message = f"You guessed all the regions! Final score: {SCORE}"

# Show the message in a pop-up window
messagebox.showinfo("Game Over", final_message)

# Close the turtle screen
screen.bye()