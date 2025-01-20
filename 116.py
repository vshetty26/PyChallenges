def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. You see two paths ahead.")
    choice1 = input("Do you go left or right? ").lower()
    
    if choice1 == "left":
        print("You encounter a river. Do you swim across or build a raft?")
        choice2 = input("Type 'swim' or 'raft': ").lower()
        if choice2 == "swim":
            print("You swam across safely. You win!")
        elif choice2 == "raft":
            print("The raft sank. You lose!")
        else:
            print("Invalid choice. You lose!")
    elif choice1 == "right":
        print("You encounter a cave. Do you enter or run away?")
        choice2 = input("Type 'enter' or 'run': ").lower()
        if choice2 == "enter":
            print("You find treasure. You win!")
        elif choice2 == "run":
            print("You got lost in the forest. You lose!")
        else:
            print("Invalid choice. You lose!")
    else:
        print("Invalid choice. You lose!")

adventure_game()
