try:
    with open("output.txt", "r") as file:
        content = file.read()
    print("File Content:\n", content)
except FileNotFoundError:
    print("'output.txt' does not exist.")
