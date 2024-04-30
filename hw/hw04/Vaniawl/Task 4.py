# def celsius_to_fahrenheit(celsius):
#     if celsius < -273.15:
#         print("error: it can not be less than -273,15°C. It is the lowest possible temperature in the universe")
#     else:
#         fahrenheit = (celsius * 9/5) + 32
#         print(f"{celsius}°C equals {fahrenheit}°F ")
#
#
#
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 1.8) + 32
# def main ()
#     try:
#         celcius = float(input("Enter temperature in Celsius: "))
#         if celcius < -273.15:
#             print("error: it can not be less than -273,15°C. It is the lowest possible temperature in the universe" )
#         else:
#             fahrenheit = celsius_to_fahrenheit(celcius)
#             print(f"{celsius}°C equals {fahrenheit}")

# def celsius_to_fahrenheit(celsius):
#     if celsius == 0 < -273.15:
#         print("error: it can not be less than -273,15°C. It is the lowest possible temperature in the universe")
#     else:
#         fahrenheit = (celsius * 1.8) + 32
#         print
#
# def main():
#     celsius = float(input("Enter temperature in Celsius: "))
#     celsius_to_fahrenheit(celsius)
# main()


def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        print("error: it can not be less than -273,15°C. It is the lowest possible temperature in the universe")
    else:
        fahrenheit = (celsius * 1.8) + 32
        print(f"{celsius}°C equals to {fahrenheit}°F")


def main():
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        celsius_to_fahrenheit(celsius)
    except ValueError:
        print("Error this input can not be converted")


if __name__ == "__main__":
    main()
