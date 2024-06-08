from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox as mb
import time

root = Tk()  # створюєм корневий об'єкт - вікно

#root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y)) # встановлюємо розміри вікна
root.title("CAT")  # встановлюємо заголовок вікна

icon = PhotoImage(file="iconCat.png")  # альтернативна опція встановлення іконки
root.iconphoto(False, icon)  # альтернативна опція встановлення іконки

logo = PhotoImage(file="cat.png")  # створюємо об'єкт зображення
logo1 = Label(image=logo)  # створюємо об'єкт зображення https://www.pythontutorial.net/tkinter/tkinter-photoimage/

game = 3  # умова продовження гри
healthCat = 20  # "здоров'я,"
leisureCat = 20  # leisure - "задоволення"
while game == 3:
    def update_clock():
        ''' функція, яка відповідає за оновлення ігрової ситуації раз на секунду '''
        now = time.strftime("%H:%M:%S")
        root.after(1000, update_clock)
        root.after(1000, heppimin)


    def heppimin():
        global healthCat  # працюємо з глобальними аргументами
        global leisureCat  # працюємо з глобальними аргументами
        if healthCat <= 0 or leisureCat <= 0:
            answer = mb.askyesno(title="You lost", message="Do you want to play again?")
            if answer == True:
                healthCat += 50
                leisureCat += 50
            else:
                game = 1
        elif healthCat >= 100 and leisureCat >= 100:
            answer2 = mb.askyesno(title="You win", message="Do you want to play again?")
            if answer2 == True:
                healthCat -= 50
                leisureCat -= 50
            else:
                game = game + 1
        healthCat = healthCat - 3  # кожної ітерації параметр "здоров'я," зменшується на 3
        leisureCat = leisureCat - 3  # кожної ітерації параметр "задоволення" зменшується на 3
        l1.configure(text="health - " + str(
            healthCat) + "%")  # змінюємо налаштування текстової мітки "здоров'я,", приводимо до стрінги та "надсилаємо" до розділу розташування віджетів 
        l2.configure(text="leisure - " + str(leisureCat) + "%")  # змінюємо налаштування текстової мітки "задоволення"


    def health():
        global healthCat
        global leisureCat
        healthCat = healthCat + 10
        leisureCat = leisureCat - 2
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        l3.configure(text="your cat is healh")
        if leisureCat <= 10:
            mb.showerror("sorry", "your cat is sad")
            leisureCat = leisureCat + 20


    def leisure():
        global healthCat
        global leisureCat
        healthCat = healthCat - 2
        leisureCat = leisureCat + 10
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        l3.configure(text="your cat is laisure")
        if healthCat <= 10:
            mb.showerror("sorry", "your cat is ill")
            healthCat = healthCat + 20


    label2 = Label(width=27, height=3, text="It is your Cat", font="Arial")
    b1 = ttk.Button(width=15, text="feed", command=health)  # годувати
    b2 = ttk.Button(width=15, text="caress", command=leisure)  # пестити
    b3 = ttk.Button(width=15, text="train", command=health)  # виховувати, тренувати
    b4 = ttk.Button(width=15, text="play", command=leisure)  # грати
    b5 = ttk.Button(width=15, text="Exit", command=quit)  # вихід
    l1 = Label(width=20, height=3, text="health - " + str(healthCat) + "%")  # здоров'я,
    l2 = Label(width=20, height=2, text="leisure - " + str(leisureCat) + "%")  # задоволення, дозвілля
    l3 = Label(width=20, height=2, text="your cat is alive")  # здоровий

    label2.grid(row=0, column=2, columnspan=3, rowspan=2)
    b1.grid(row=2, column=0)
    b2.grid(row=3, column=0)
    b3.grid(row=4, column=0)
    b4.grid(row=5, column=0)
    b5.grid(row=9, column=3)
    l1.grid(row=6, column=0)
    l2.grid(row=7, column=0)
    l3.grid(row=7, column=3)
    logo1.grid(row=2, column=2, columnspan=5, rowspan=5)

    update_clock()
    root.mainloop()  # Для відображення вікна та взаємодії з користувачем у вікна викликається метод mainloop()
