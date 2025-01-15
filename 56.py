sentence = input("Enter a sentence: ")
words = sentence.split()
print(max(words, key=len))
