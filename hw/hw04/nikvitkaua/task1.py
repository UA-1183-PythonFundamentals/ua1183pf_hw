celsius_from_user = float(input("Enter the temperature in Celsius: "))
celsius_as_fahrenheit = (celsius_from_user * 9/5) + 32

match celsius_from_user:
    case x if x < -273.15:
        print('Error: Temperature below absolute zero (-273.15°C)')
    case _:
        print(f"{celsius_from_user}°C is equivalent to {celsius_as_fahrenheit}°F")