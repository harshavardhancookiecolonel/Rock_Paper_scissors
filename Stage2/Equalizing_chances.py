import random

def Equalizing_chances():
    choices = ['rock', 'paper', 'scissors']
    user_choice = str(input())
    computer_choice = random.choice(choices)


    if user_choice == computer_choice:
        print('This is a draw ' + (user_choice))
    elif ((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock")or (user_choice == "scissors" and computer_choice == "paper") ):
        print("Well done. The computer chose " + computer_choice + " and failed")
    else:
        print("Sorry, but the computer chose " + computer_choice)

Equalizing_chances()


