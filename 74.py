file_name = input("Enter file name: ")
try:
    with open(file_name, "r") as file:
        line_count = sum(1 for line in file)
    print(f"Total Lines: {line_count}")
except FileNotFoundError:
    print(f"'{file_name}' does not exist.")
