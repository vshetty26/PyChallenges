def lcm_up_to_n(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1): 
            if num % i == 0:
                return False
        return True

    def highest_power(p, n):
        power = p
        while power * p <= n:
            power *= p
        return power

    lcm = 1
    for p in range(2, n + 1):
        if is_prime(p):
            lcm *= highest_power(p, n)
    return lcm

try:
    n = int(input("Enter the number: "))
    print("LCM of numbers from 1 to", n, "is:", lcm_up_to_n(n))
except ValueError:
    print("Please enter a valid integer.")
