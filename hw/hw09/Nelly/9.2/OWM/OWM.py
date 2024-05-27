# OWM.py

def get_weather(city_name):
    api_key = "426a10cee87410f390caea13b402b8b3"  # Replace "YOUR_API_KEY" with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        weather_info = f"Weather in {city_name}:\n"
        weather_info += f"Temperature: {data['main']['temp']}°C\n"
        weather_info += f"Description: {data['weather'][0]['description']}"
        return weather_info
    else:
        raise Exception(f"Error: {data['message']}")
