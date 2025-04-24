import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return None

    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

wins = 0
losses = 0
ties = 0

while True:
    result = play_game()
    if result == "You win!":
        wins += 1
    elif result == "You lose!":
        losses += 1
    elif result == "It's a tie!":
        ties += 1
    
    print(f"Score -> Wins: {wins} | Losses: {losses} | Ties: {ties}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
