# Combined_OWM.py


import tkinter as tk
from tkinter import messagebox
from OWM import get_weather  

def get_weather_info():
    city_name = city_entry.get()
    try:
        weather_info = get_weather(city_name)
        messagebox.showinfo("Weather Info", weather_info)
    except Exception as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.title("Weather App")

city_label = tk.Label(window, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

get_weather_button = tk.Button(window, text="Get Weather", command=get_weather_info)
get_weather_button.pack()

window.mainloop()
