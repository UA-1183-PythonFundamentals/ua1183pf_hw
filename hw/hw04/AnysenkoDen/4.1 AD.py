celsius = int(input('Enter the temperature in Celsius: :'))
farenheit = (celsius * 9/5) + 32

if farenheit >= (-273.15): 
    print(f'{celsius}°C is equivalent to {farenheit}°F') 
else:
    print('Error: Temperature below absolute zero (-273.15°C)')