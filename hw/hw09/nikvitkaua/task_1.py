from tkinter import *
from tkinter import ttk
import re
from random import randint
import os
import sys

root = Tk()
root.geometry('600x400')
root.title('GUESS A NUMBER')

# Variables
RANDOM_NUM = randint(1, 100)
btn_click = 0
label_title = Label(text="Guess a number from 1 to 100 for 10 tries", font=72)
label_wrong = Label(root, font=("Arial", 12), fg="red")

print(RANDOM_NUM)

# Functions
def get_input():
    global btn_click
    btn_click += 1
    user_input = entry.get()

    if is_numeric(user_input) or user_input == '':
        label_wrong.config(text=f"This shit is not numeric, please try again, u do {btn_click} tries")
    elif not (0 < int(user_input) <= 100):
        label_wrong.config(text=f"This shit is not in range, u do {btn_click} tries")
    elif int(user_input) < RANDOM_NUM:
        label_wrong.config(text=f"This number is low, u do {btn_click} tries. Try again!")
    elif int(user_input) > RANDOM_NUM:
        label_wrong.config(text=f"This number is high, u do {btn_click} tries. Try again!")
    else:
        label_wrong.config(text=f"Success! You enter {user_input} and win!", fg="green")
        button_restart_program.pack()

    return {
        "value": user_input,
        "counter": btn_click
    }

def is_numeric(string):
    return bool(re.search(r'\D', string))

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# UI
# Title
label_title.pack()

# Input
entry = Entry(root, font=24)
entry.pack(pady=20)

# Button
button = Button(root, text="GUESS", command=get_input)
button.pack()

# Error or success message
label_wrong.pack(pady=20)

# Restart btn
button_restart_program = Button(root, text="Restart", command=restart_program)

root.resizable(False, False)

root.mainloop()