import tkinter as tk
from tkinter import font
from program import Country

HEIGHT = 760
WIDTH = 1024


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,  bg="pink")
root.title("Country info helper")
canvas.pack()



frame = tk.Frame(root, bg="pink", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

def get_information(country_name):
    info = Country(country_name)
    label.config(text=info.get_country_info())
       

button = tk.Button(frame, 
                   text="Get Info", 
                   bg="gray", fg="white", 
                   font=('Courier', 14), 
                   command=lambda: get_information(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='light blue', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()