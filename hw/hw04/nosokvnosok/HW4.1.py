# temperature converter
tempCel = float(input("Enter temperature in Celsius: "))

if tempCel >= -273.15:
    print(f"{tempCel} in Celsius equals {tempCel * (9/5) + 32} in Fahrenheit")
else:
    print("Error: Temperature below absolute zero (-273.15°C)")
