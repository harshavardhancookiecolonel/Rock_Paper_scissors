import random

# Read the user's choice
user_choice = input()

# Generate a random choice for the computer
computer_choice = random.choice(["rock", "paper", "scissors"])

# Define a function to determine the winning choice for the computer
def computer_wins(user_choice):
    if user_choice == "rock":
        return "paper"
    elif user_choice == "paper":
        return "scissors"
    elif user_choice == "scissors":
        return "rock"
    else:
        return None

# Check if the user's choice is valid
if user_choice in ["rock", "paper", "scissors"]:
    # Determine the computer's winning choice
    computer_winning_choice = computer_wins(user_choice)

    # Output the result
    if computer_winning_choice:
        print(f"Sorry, but the computer chose {computer_winning_choice}")
    else:
        print("Invalid input. Please choose rock, paper, or scissors.")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")


