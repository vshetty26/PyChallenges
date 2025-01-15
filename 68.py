num = input("Enter a number: ")
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
print(" ".join(words[int(d)] for d in num))
