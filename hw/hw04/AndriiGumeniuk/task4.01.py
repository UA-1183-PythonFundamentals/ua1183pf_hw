temperature_celsius = float(input("Enter the temperature in Celsius: "))

if temperature_celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    print(f"{temperature_celsius}°C is equivalent to {temperature_fahrenheit}°F")
