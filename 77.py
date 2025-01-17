file_name = input("Enter file name: ")
word = input("Enter word to search: ")
try:
    with open(file_name, "r") as file:
        lines = file.readlines()
    found_lines = [i + 1 for i, line in enumerate(lines) if word in line]
    if found_lines:
        print(f"Word found on line(s): {found_lines}")
    else:
        print("Word not found.")
except FileNotFoundError:
    print(f"'{file_name}' does not exist.")
