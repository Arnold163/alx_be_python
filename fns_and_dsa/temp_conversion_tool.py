# Global conversion tool
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 5 / 9 # Corrected variable name with "S" in Celsius and value
FAHRENHEIT_FREEZING_POINT = 32
CELSIUS_FREEZING_POINT = 32

# function for conversion
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# function for conversion
def convert_to_fahrenheit(celsius):
    # Use CELSIUS_TO_FAHRENHEIT_FACTOR (correct spelling)
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# main function
def main():
    try:
        temp = float(input("Enter the temperature: "))
        unit = input("Is the temperature in (C)elsius or (F)ahrenheit? ").strip().upper()  # Fixed typo in the input prompt
        
        if unit == "C":
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp:.2f}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
    except ValueError as e:
        print(f"Invalid input: {e}")

# call main function
if __name__ == "__main__":
    main()