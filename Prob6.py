def divide_numbers(dividend, divisor):
    if divisor == 0:
        return "Error: Division by zero is not allowed"
    else:
        return dividend / divisor


try:
    dividend = float(input("Enter the Dividend: "))
    divisor = float(input("Enter the Divisor: "))
    print(divide_numbers(dividend, divisor))
except ValueError:
    print("Error: Please enter a valid number")
