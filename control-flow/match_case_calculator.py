# ask user input 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("choose the operation (+, -, *, /): ")

# match case operation
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2 
    case "/":
        result = num1 / num2
        if num2 == 0:
            result = "error: Division by zero is not allowed."
        else:
            result = num1 / num2
    case _:
        result = "Invalid operation"

if isinstance(result, str):
    print(result)
else:
    print(f"The result is: {result}")