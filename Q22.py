def power(base,exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result 
    return result

base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")
