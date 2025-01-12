def prime(n):
    if n<= 1:
        return False
    for i in range(2, int(n** 0.5) + 1):
        if n% i == 0:
            return False
    return True

n = int(input("Enter num"))
if prime(n):
    print(f"{n} is prime num")
else:
    print(f"{n} is not prime num")
