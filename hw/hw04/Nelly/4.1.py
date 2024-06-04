# user_input = float(input("Enter the temperature in Celsius: "))

# if user_input < -273.15:
#     print("Error: Temperature below absolute zero (-273.15°C)")
# else:
#     fahrenheit = (user_input * 9/5) + 32
#     print(f"{user_input}°C is equivalent to {fahrenheit}°F")



try:
    user_input = float(input("Enter the temperature in Celsius: "))
    if user_input < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
    else:
        fahrenheit = (user_input * 9/5) + 32
        print(f"{user_input}°C is equivalent to {fahrenheit}°F")
except:
    print("Error")

