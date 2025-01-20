import random

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please choose from 'rock', 'paper', or 'scissors'.")
        return
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

rock_paper_scissors()
