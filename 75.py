file_name = input("Enter file name: ")
try:
    with open(file_name, "r") as file:
        word_count = sum(len(line.split()) for line in file)
    print(f"Total Words: {word_count}")
except FileNotFoundError:
    print(f"'{file_name}' does not exist.")
