def Fibonacci(n):
    if n == 0 or n == 1:
        return n
    elif n < 0:
        return ValueError("Enter Positive Number")
    return Fibonacci(n - 1) + Fibonacci(n - 2)


n = int(input("Enter n:"))
print(Fibonacci(n))
