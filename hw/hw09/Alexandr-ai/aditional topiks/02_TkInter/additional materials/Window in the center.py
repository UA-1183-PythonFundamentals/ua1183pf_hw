# Розташування вікна по центру екрана
from tkinter import *
root = Tk()
 
Button(text="Button", width=20).pack()
Label(text="Label", width=20, height=3).pack()
Button(text="Button", width=20).pack()
 
root.update_idletasks()
s = root.geometry()
s = s.split('+')
s = s[0].split('x')
width_root = int(s[0])
height_root = int(s[1])
 
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2 
w = w - width_root // 2
h = h - height_root // 2
root.geometry('+{}+{}'.format(w, h))
 
root.mainloop()
