import random

def Equalizing_chances():
    choices = ['rock', 'paper', 'scissors', '!exit']
    
    while True:
        user_choice = input()
        
        if user_choice == '!exit':
            print("Bye!")
            break 
        elif user_choice != random.choice(choices):
            print("Invalid input")
        
        computer_choice = random.choice(choices[:-1]) 
        
        if user_choice == computer_choice:
            print(f'This is a draw. Both chose ({user_choice})')
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            print(f"Well done. The computer chose {computer_choice} and failed.")
        else:
            print(f"Sorry, but the computer chose {computer_choice}.")

Equalizing_chances()
