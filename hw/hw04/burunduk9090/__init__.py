temp_c = float(input('Enter temperature in Celsius: '))
temp_f = temp_c * 9/5 + 32
result = f"{temp_c}°C = {temp_f}°F" if temp_c > -273.15 else 'Error, temperature less than absolute zero(-273.15)'


rint(result)

