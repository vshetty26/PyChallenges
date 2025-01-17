file_name = input("Enter file name: ")
new_file_name = input("Enter new file name: ")
try:
    with open(file_name, "r") as file:
        lines = file.readlines()
    with open(new_file_name, "w") as new_file:
        new_file.writelines(line for line in lines if line.strip())
    print("Blank lines removed and saved to new file.")
except FileNotFoundError:
    print(f"'{file_name}' does not exist.")
