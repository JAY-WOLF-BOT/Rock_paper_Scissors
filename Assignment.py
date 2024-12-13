import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        return

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")