import math
n = int(input("Enter a number: "))
digits = [int(d) for d in str(n)]
print(n == sum(math.factorial(d) for d in digits))
