import tkinter as tk
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)

HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


def get_weather(city):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    temperature = weather.temperature('celsius')
    humidity = weather.humidity
    detailed_status = weather.detailed_status
    rain = weather.rain
    clouds = weather.clouds
    wind = weather.wind()

    return (f'Max_temp: {temperature['temp_max']}\n'
            f'Min_temp: {temperature['temp_min']}\n'
            f'Temp: {temperature['temp']}\n'
            f'Rain: {rain if rain else None}\n'
            f'Humidity: {humidity}\n'
            f'Detailed Status: {detailed_status}\n'
            f'Clouds: {clouds}\n'
            f'Wind: {wind['speed']}km/h\n')


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Time New Roman', 12))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: label.config(text=get_weather(entry_field.get()), justify='left'))

button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

root.mainloop()