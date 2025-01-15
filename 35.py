lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
positive = len([i for i in lst if i > 0])
negative = len([i for i in lst if i < 0])
zero = len([i for i in lst if i == 0])
print(positive, negative, zero)

