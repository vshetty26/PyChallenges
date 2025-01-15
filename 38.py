def reverse_list(lst):
    lst.reverse()
    return lst

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(reverse_list(lst))
