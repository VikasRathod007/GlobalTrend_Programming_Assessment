def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator. Use '+', '-', '*', or '/'."


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator: ")
    result = calculate(num1, num2, operator)
    print(f"Result: {result}")
except ValueError:
    print("Error: please enter a valid number")
