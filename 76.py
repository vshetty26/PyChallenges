file_name = input("Enter file name: ")
try:
    with open(file_name, "r") as file:
        longest_line = max(file, key=len)
    print("Longest Line:\n", longest_line.strip())
except FileNotFoundError:
    print(f"'{file_name}' does not exist.")
