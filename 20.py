num = int(input("Enter a positive integer: "))
print("Palindrome" if str(num) == str(num)[::-1] else "Not a Palindrome")