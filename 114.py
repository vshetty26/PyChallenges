import random

words = ["python", "hangman", "programming", "developer", "computer"]
word_to_guess = random.choice(words)
word_length = len(word_to_guess)

guessed_word = ["_"] * word_length
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print(f"The word has {word_length} letters: {' '.join(guessed_word)}")

while attempts > 0 and "_" in guessed_word:
    print(f"\nAttempts remaining: {attempts}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Correct guess!")
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[index] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

    print(f"Word: {' '.join(guessed_word)}")

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word!")
else:
    print("\nYou ran out of attempts!")
    print(f"The word was: {word_to_guess}")
