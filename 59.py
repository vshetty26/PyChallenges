import string
s = input("Enter a string: ")
special_chars = set(string.punctuation)
count = sum(1 for char in s if char in special_chars)
print(count)
