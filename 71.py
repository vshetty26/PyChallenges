content = input("Enter a string: ")
with open("output.txt", "w") as file:
    file.write(content)
print("Content written to 'output.txt'.")
