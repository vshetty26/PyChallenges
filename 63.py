n = int(input("Enter a number: "))
divisors = [i for i in range(1, n) if n % i == 0]
print(n == sum(divisors))
