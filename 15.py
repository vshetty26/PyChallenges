num = int(input("Enter a non-negative integer: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)