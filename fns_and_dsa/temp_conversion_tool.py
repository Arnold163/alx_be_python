import sys

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction
try:
    temp = float(input("Enter a temperature: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()
    if unit == "C":
        print(f"{temp} degrees Celsius is equal to {convert_to_fahrenheit(temp)} degrees Fahrenheit.")
    elif unit == "F":
        print(f"{temp} degrees Fahrenheit is equal to {convert_to_celsius(temp)} degrees Celsius.")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")