n = int(input("Enter a positive integer: "))
even_sum = sum(i for i in range(1, n + 1) if i % 2 == 0)
odd_sum = sum(i for i in range(1, n + 1) if i % 2 != 0)
print(even_sum, odd_sum)