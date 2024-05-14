from pyowm import OWM
import tkinter as tk
from tkinter import font


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
    city = entry_field.get()
    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(city)
    w = observation.weather

    weather_info = f"Clouds: {w.detailed_status}\n "       # 'clouds'
    weather_info += f"Wind: {w.wind()}\n " #print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    weather_info += f"Humidity: {w.humidity}\n " #print(w.humidity)                # 87
    weather_info += f"Temperature: {w.temperature('celsius')}\n" #print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    weather_info += f"Rain: {w.rain}\n " #print(w.rain)                    # {}
    weather_info += f"Heat index: {w.heat_index}\n " #print(w.heat_index)              # None
    weather_info += f"Clouds posibility: {w.clouds}\n " #print(w.clouds)                  # 75

    label['text'] = weather_info


HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command= get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14), justify='left', anchor='nw')
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()