import random

user_choice = input("Enter a choice (rock, paper, scissors): ")

moves = ["rock", "paper", "scissors"]
computer_move = random.choice(possible_actions)

if user_choice == computer_move:
    print(f"Both players selected {user_action}. Try Again!")
    user_choice = input("Enter a choice (rock, paper, scissors): ")

elif user_choice == "rock":
    if computer_move == "scissors":
        print("Scissors cannot cut rock. Rock breaks scissors. You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_choice == "paper":
    if computer_move == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_choice == "scissors":
    if computer_move == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Scissors cannot cut rock. Rock breaks scissors. You lose.")
