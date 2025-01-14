def count_occurrences(lst, x): return lst.count(x)
lst = list(map(int, input("Enter list elements separated by space:").split()))
x = int(input("Enter element to count: "))
print(count_occurrences(lst, x))