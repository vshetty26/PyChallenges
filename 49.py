lst1 = set(map(int, input("Enter first list of numbers: ").split()))
lst2 = set(map(int, input("Enter second list of numbers: ").split()))
print(lst1 | lst2)
print(lst1 & lst2)
print(lst1 - lst2)
