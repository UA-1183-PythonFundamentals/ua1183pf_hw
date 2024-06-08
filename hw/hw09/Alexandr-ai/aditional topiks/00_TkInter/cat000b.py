from tkinter import *
from tkinter import ttk

root = Tk()                         # створюєм корневий об'єкт - вікно
root.geometry('400x300')            # встановлюємо розміри вікна
root.title("CAT")                   # встановлюємо заголовок вікна

icon = PhotoImage(file = "iconCat.png") # альтернативна опція встановлення іконки
root.iconphoto(False, icon)         # альтернативна опція встановлення іконки

logo = PhotoImage(file="cat.png")   # створюємо об'єкт зображення
logo1 = Label(image=logo)           # створюємо об'єкт зображення 

for r in range(3):
	for c in range(3):
		btn = ttk.Button(text=f"({r},{c})")
		btn.grid(row=r, column=c)
 
label = Label(text="Hello, world!") # створюємо текстову мітку
#label.pack()    		    # розміщуємо мітку у вікні
label.grid(row=4, column=4)
root.resizable(False, False)




root.mainloop() 		    # Для відображення вікна треба викликати в нього метод mainloop() , який запускає цикл обробки 	подій вікна взаємодії з користувачем.
