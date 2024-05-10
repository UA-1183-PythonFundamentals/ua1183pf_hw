from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
def get_weather(city_name):
    try:
        observation = mgr.weather_at_place(f"{city_name}")
        w = observation.weather
        status = w.detailed_status
        wind_speed = w.wind()['speed']
        wind_deg = w.wind()['deg']
        humidity = w.humidity
        temp = w.temperature('celsius')['temp']
        clouds = w.clouds

        result = f"City: {city_name}\n Status: {status}\n Wind speed: {wind_speed}\n Wind degree: {wind_deg}\n Humidity: {humidity}\n Temperature: {temp}\n Clouds: {clouds}"

        return result
    except Exception as e:
        return "City not found"

  
  



