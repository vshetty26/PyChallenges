lst1 = list(map(int, input("Enter first list of numbers: ").split()))
lst2 = list(map(int, input("Enter second list of numbers: ").split()))
print([x + y for x, y in zip(lst1, lst2)])
