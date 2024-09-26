# global conversion tool
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELCIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

#function for conversion
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * CELCIUS_TO_FAHRENHEIT_FACTOR

#function for conversion
def convert_to_fahrenheit(celsius):
    return (celsius * CELCIUS_TO_FAHRENHEIT_FACTOR) + 32

#main function
def main():
    try:
        temp = float(input("Enter the temperature: "))
        unit = input("ïs the tempereture in (C)elsius or (F)ahrenheit? ").strip().upper()
        
        if unit == "C":
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp: .2f}°F")
        elif unit == "F":
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp: .2f}°C")
        else:
            raise ValueError("invalid unit. please enter 'C' for celcius of 'F' for fahrenheit.")
        
    except ValueError as e:
        print(f"invalid input: {e}")
    

#call main function
if __name__ == "__main__":
    main()  
    