def load_dictionary(file_name):
    dictionary = {}
    with open(file_name, 'r') as file:
        for line in file:
            word, definition = line.strip().split(": ", 1)
            dictionary[word.lower()] = definition
    return dictionary

def search_word(dictionary, word):
    word = word.lower()
    if word in dictionary:
        print(f"Definition of {word}: {dictionary[word]}")
    else:
        print(f"Sorry, the word '{word}' is not in the dictionary.")

def main():
    dictionary = load_dictionary('dictionary.txt')

    while True:
        word = input("Enter a word to search (or type 'exit' to quit): ").strip()
        
        if word.lower() == 'exit':
            print("Exiting the dictionary app.")
            break
        
        search_word(dictionary, word)

main()
