lst1 = list(map(int, input("Enter first list of numbers: ").split()))
lst2 = list(map(int, input("Enter second list of numbers: ").split()))
print(list(set(lst1) & set(lst2)))
