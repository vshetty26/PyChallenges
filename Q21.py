def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

num1 = float(input("Enter first num: "))
num2 = float(input("Enter second num: "))
operation = input("Choose (add, subtract, multiply, divide): ")

if operation == "add":
    print("Result:", add(num1, num2))
elif operation == "subtract":
    print("Result:", subtract(num1, num2))
elif operation == "multiply":
    print("Result:", multiply(num1, num2))
elif operation == "divide":
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation")
