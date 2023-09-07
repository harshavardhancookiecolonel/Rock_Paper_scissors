import random

def Equalizing_chances():
    choices = ['rock', 'paper', 'scissors', '!exit', '!rating']
    user_name = input("Enter your name: ")
    print("Hello, " + user_name)
    
    user_score = 0
    
    try:
        with open('rating.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, score = line.strip().split()
                if name == user_name:
                    user_score = int(score)
                    break
    except FileNotFoundError:
        pass
    
    while True:
        user_choice = input()
    
        if user_choice == '!rating':
            print("Your rating: " + str(user_score))
    
        if user_choice == '!exit':
            print("Bye!")
            break
        elif user_choice not in choices[:-2]:  # Check if the choice is valid
            print("Invalid input")
            continue
    
        computer_choice = random.choice(choices[:-2])
    
        if user_choice == computer_choice:
            user_score += 50
            print(f'This is a draw. Both chose ({user_choice})')
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "rock")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            user_score += 100
            print(f"Well done. The computer chose {computer_choice} and failed.")
        else:
            print(f"Sorry, but the computer chose {computer_choice}.")
    
    with open("rating.txt", "a") as file:
        file.write(f"{user_name} {user_score}\n")

Equalizing_chances()
