c = int(input("Enter the temperature in celsius: "))

convert = int((c * 9/5) + 32)

if(convert > -273.15):
    print(f"{c}C is equivalent to {convert}F")
elif(convert < -273.15):
    print("Error: Temperature below absolute zero (-273.15C)")