def celsius_to_fahrenheit(celsius):
    # Check if temperature is below absolute zero
    if celsius < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
    else:
        # Convert Celsius to Fahrenheit
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equivalent to {fahrenheit}°F")

def main():
    # Prompt the user for input
    celsius = float(input("Enter the temperature in Celsius: "))
    # Convert temperature to Fahrenheit
    celsius_to_fahrenheit(celsius)

if __name__ == "__main__":
    main()
