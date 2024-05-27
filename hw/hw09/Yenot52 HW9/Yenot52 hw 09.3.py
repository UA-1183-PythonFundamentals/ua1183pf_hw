import tkinter as tk
from tkinter import font
from pyowm.owm import OWM 

API_KEY = 'ef2206ff5da67de63306d0b143e20872' 

HEIGHT = 350
WIDTH = 450

def get_weather():
    city = entry_field.get()  # Get city name from entry field
    if not city:
        label.config(text="Please enter a city name.")
        return

    # Use OpenWeatherMap API to get weather data
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(city)  # Search by city
        w = observation.weather

        # Extract and format weather details
        status = w.detailed_status.title()  # Capitalize the first letter
        wind_speed = f"Wind Speed: {w.wind()['speed']} m/s"
        humidity = f"Humidity: {w.humidity}%"
        temperature = w.temperature('celsius')  # Get temperature dictionary
        temp_min = f"Min Temp: {temperature['temp_min']:.1f}°C"
        temp_max = f"Max Temp: {temperature['temp_max']:.1f}°C"
        clouds = f"Clouds: {w.clouds}%"

        # Update the label with formatted weather data
        weather_info = f"\nCity: {city}\nStatus: {status}\n{wind_speed}\n{humidity}\n{temp_min}\n{temp_max}\n{clouds}"
        label.config(text=weather_info)

    except Exception as e:
        print(f"Error retrieving weather data: {e}")
        label.config(text="Error fetching weather data. Check city name or API key.")

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
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), text="")
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()