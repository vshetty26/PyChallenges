n = int(input("Enter a number: "))
digits = [int(d) for d in str(n)]
print(n == sum(d**len(digits) for d in digits))
