target_number = int(input("Set the target number (between 1 and 100): "))
guess = int(input("Guess the number (between 1 and 100): "))
while guess != target_number:
    if guess < target_number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))
print("Correct!")
