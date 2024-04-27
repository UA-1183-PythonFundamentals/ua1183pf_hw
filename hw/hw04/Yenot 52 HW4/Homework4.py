def celsius_to_fahrenheit(celsius):
  """Converts a temperature in Celsius to Fahrenheit.
  
  Args:
      celsius: The temperature in Celsius.

  Returns:
      The temperature in Fahrenheit, or an error message if below absolute zero. 
  """ 
  if celsius < -273.15:
    return"Error: Temperature below absolute zero (-273.15°C)"
  else:
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C is equivalent to {round(fahrenheit, 2)}°F" 

celsius_temperature = float(input("Enter the temperature in Celsius: \n"))
result = celsius_to_fahrenheit(celsius_temperature)
print(result)