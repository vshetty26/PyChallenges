source = input("Enter source file name: ")
destination = input("Enter destination file name: ")
try:
    with open(source, "r") as src, open(destination, "w") as dest:
        dest.write(src.read())
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file does not exist.")
