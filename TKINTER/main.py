from tkinter import *
import math
from tkinter import messagebox
from random import randint
import pyperclip
from datetime import datetime

count_min = 0
count_sec = 0
count = None
random_number = None
timer = None
player_guesses = []  # Store player's guesses
btnnr = []  # Store player's Numbers

for i in range(1, 21):
    player_guesses.append(None)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Guess 20")
window.config(padx=50, pady=50)
window.tk.call("source", "Azure/azure.tcl")


# Set the theme using the theme_use method
window.tk.call("set_theme", "light")


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    messagebox.showinfo("RESET GAME", "you restarted game. Try agen :)")
    b0.config(state=NORMAL)
    global btnnr

    player_guesses.clear()

    for i in range(1, 21):
        player_guesses.append(None)

    for i in btnnr:
        i.config(text="")

    b0.config(text="Start", command=start_timer)
    canvas.itemconfig(timer_text, text="0:00")

    for button in btnnr:
        button.config(state=DISABLED)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global timer
    count_up(0)
    num_generator()
    b0.config(text="Generate Num", command=num_generator)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_up(count):
    global count_min, count_sec

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    global timer
    timer = window.after(1000, count_up, count + 1)


# ---------------------------- RANDOM NUMBER ------------------------------- #
def num_generator():
    global random_number
    random_number = randint(0, 1000)
    rndNum.config(text=random_number)
    pyperclip.copy(str(random_number))
    b0.config(state=DISABLED)

    for button in btnnr:
        button.config(state=NORMAL)



def create_nr():
    for i in range(1, 21):
        nr1 = Label(text=i, font=("Calibri", 14))
        nr1.grid(column=0, row=i)

# LABELS
label = Label(text="RANDOM", padx=300, font=("Calibri", 35, "bold"))
label.grid(column=3, row=0)

label2 = Label(text="20", padx=300, font=("Calibri", 50, "bold"))
label2.grid(column=3, row=2)

rndNum = Label(text="000", font=("Calibri", 35, "bold"))
rndNum.grid(column=3, row=8)

label3 = Label(text="Time", padx=300, font=("Calibri", 35, "bold"))
label3.grid(column=3, row=15)

canvas = Canvas(width=200, height=224)
timer_text = canvas.create_text(100, 130, text="00:00", font=("Calibri", 35, "bold"))
canvas.grid(column=3, row=17)


def create_entry():
    for i in range(1, 21):
        buttons = Button(text="", width=5, command=lambda i=i: update_button_text(i))
        buttons.grid(column=1, row=i)
        btnnr.append(buttons)




def update_button_text(i):
    clipboard_text = pyperclip.paste()
    try:
        clipboard_text = int(clipboard_text)
    except ValueError:
        # Handle invalid input (non-integer clipboard contents)
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")
        return

    button = btnnr[i-1]  # Use the index directly from the loop
    button.config(text=clipboard_text)
    # Find the index of the button within the btnnr list
    index_in_btnnr = btnnr.index(button)

    # Insert the guess at the calculated insert_index
    clipboard_number = int(clipboard_text)
    player_guesses[index_in_btnnr] = clipboard_number  # Use index_in_btnnr directly as the index

    # Disable all buttons to prevent further input from the player after making a guess
    for button in btnnr:
        button.config(state=DISABLED)

    # Enable the button with index b0 to initiate the next turn or start the game
    b0.config(state=NORMAL)

    check_order()  # Automatically check the order after each turn




def check_order():

    # Filter out None values from the player_guesses list
    filtered_guesses = [guess for guess in player_guesses if guess is not None]

    if len(filtered_guesses) == 20 and filtered_guesses == sorted(filtered_guesses):
        checkmarks.config(text="Congratulations!")
        window.after_cancel(timer)
        messagebox.showinfo("Game Over", f"Congratulations! You guessed all the numbers correctly. Your time is - {count_min}:{count_sec}")

        file = open("victorys.txt", "a")
        this = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        file.write(this+f"  Your time is - {count_min}:{count_sec}\n")



        reset_timer()
    elif filtered_guesses == sorted(filtered_guesses):
        print()
    else:
        window.after_cancel(timer)
        b0.config(state=DISABLED)
        messagebox.showinfo("Game Over", "Sorry, you did not guess the numbers in increasing order.")




# Buttons
b0 = Button(text="Start", command=start_timer)
b0.grid(column=3, row=13)

b1 = Button(text="Reset", command=reset_timer)
b1.grid(column=3, row=12)

checkmarks = Label(font=("Calibri", 14))
checkmarks.grid(column=2, row=1, columnspan=1)

create_nr()
create_entry()
window.mainloop()
