#import the package for simulating comp choices
import random

while True:
    #take input from the user and assign it to a var based on the respective choice
    user_choice = input("Enter a choice from either: rock, paper and scissors. ")

    #make the computer select a random choice between the actions
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    #print the choices that the user made vs the choice that the computer made
    print(f"\nYou chose {user_choice}, computer chose {computer_action}.\n")

    #determine a winner using a simple if elif and else block
    if user_choice == computer_action:
        print(f"Both players selected {user_choice}. It's a tie! \nGo again!")
    elif user_choice == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! Player wins; computer loses!")
        else:
            print("Paper covers rock! Player loses; computer wins!")
    elif user_choice == "paper":
        if computer_action == "rock":
            print("Paper covers rock! Player wins; computer loses!")
        else:
            print("Scissors cut paper! Player loses; computer wins!")
    elif user_choice == "scissors":
        if computer_action == "paper":
            print("Scissors cut paper! Player wins; computer loses!")
        else:
            print("Rock smashes scissors! Player loses; computer wins!")
    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() != "y":
        break