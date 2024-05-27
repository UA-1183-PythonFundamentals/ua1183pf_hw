from tkinter import *
from tkinter import ttk
import random


root = Tk()                         # створюєм корневий об'єкт - вікно
root.geometry('400x300')            # встановлюємо розміри вікна
root.title("CAT")                   # встановлюємо заголовок вікна

icon = PhotoImage(file = "iconCat.png") # альтернативна опція встановлення іконки
root.iconphoto(False, icon)         # альтернативна опція встановлення іконки

logo = PhotoImage(file="cat.png")   # створюємо об'єкт зображення
logo1 = Label(image=logo)           # створюємо об'єкт зображення https://www.pythontutorial.net/tkinter/tkinter-photoimage/

   

label2= Label(width=27,height=3, text = "It is your Cat", font="Arial")
b1 = ttk.Button(width=15,text="feed")   # годувати
b2 = ttk.Button(width=15,text="caress") # пестити
b3 = ttk.Button(width=15,text="train")  # виховувати, тренувати
b4 = ttk.Button(width=15,text="play")   # грати
l1 = Label(width=20,height=3, text = "health - %")          # здоров'я, 
l2 = Label(width=20,height=2, text = "leisure - %")         # задоволення, дозвілля
l3 = Label(width=20,height=2, text = "your cat is healthy") # здоровий



label2.grid(row=0, column=2,columnspan=3,rowspan=2)
b1.grid(row=2, column=0)
b2.grid(row=3, column=0)
b3.grid(row=4, column=0)
b4.grid(row=5, column=0)
l1.grid(row=6, column=0)
l2.grid(row=7, column=0)
l3.grid(row=7, column=3)
logo1.grid(row=2, column=2,columnspan=5,rowspan=5)


root.mainloop() # Для відображення вікна та взаємодії з користувачем у вікна викликається метод mainloop()
