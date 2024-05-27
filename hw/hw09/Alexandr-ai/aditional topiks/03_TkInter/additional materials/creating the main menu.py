from tkinter import *                             # імпортування графічної бібліотеки


root = Tk()                                       # створення головного вікна
root.geometry("200x150")                          # задання розмірів вікна


mainmenu = Menu(root)                             # створення головного меню
root.config(menu=mainmenu)


filemenu = Menu(mainmenu, tearoff=0)              # створення підменю "Файл"
filemenu.add_command(label="Новий")               # додавання команди "Новий" до підменю "Файл"
filemenu.add_command(label="Відкрити...")         # додавання команди "Відкрити..." до підменю "Файл"
filemenu.add_separator()                          # вставлення горизонтального роздільника
filemenu.add_command(label="Вихід")               # додавання команди "Вихід" до підменю "Файл"


helpmenu = Menu(mainmenu, tearoff=0)              # створення підменю "Довідка"



mainmenu.add_cascade(label="Файл", menu=filemenu)           # підв'язуємо підменю "Файл" до головного меню
mainmenu.add_cascade(label="Довідка", menu=helpmenu)        # підв'язуємо підменю "Довідка" до головного меню


root.mainloop()                                 # задання команди відображення вікна при запуску
