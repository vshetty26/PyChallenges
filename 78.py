content = input("Enter text to append: ")
with open("output.txt", "a") as file:
    file.write("\n" + content)
print("Content appended to 'output.txt'.")
