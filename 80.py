file_name = input("Enter file name: ")
try:
    with open(file_name, "r") as file:
        content = file.read()
    lines = content.splitlines()
    words = content.split()
    characters = len(content)
    print(f"Total Characters: {characters}")
    print(f"Total Words: {len(words)}")
    print(f"Total Lines: {len(lines)}")
except FileNotFoundError:
    print(f"'{file_name}' does not exist.")
