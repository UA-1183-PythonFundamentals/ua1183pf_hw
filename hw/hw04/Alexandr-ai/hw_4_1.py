

c = float(input('Enter the temperature in Celsius: :'))
f = (c * 9/5) + 32

    
#print("f :", f)
if f >= float(-273.15): 
    print(f'{c}°C is equivalent to {f}°F') 
else:
    print('Error: Temperature below absolute zero (-273.15°C)')
