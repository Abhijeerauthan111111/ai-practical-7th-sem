import random

def get_player_choice():
    while True:
        choice = input("Enter your choice (stone/paper/scissors): ").lower()
        if choice in ['stone', 'paper', 'scissors']:
            return choice
        print("Invalid choice! Please try again.")

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    winning_combinations = {
        'stone': 'scissors',
        'paper': 'stone',
        'scissors': 'paper'
    }
    if winning_combinations[player] == computer:
        return "You win!"
    return "Computer wins!"
def play_game():
    print("\n=== Stone Paper Scissors Game ===")
    print("Rules:")
    print("- Stone beats Scissors")
    print("- Paper beats Stone")
    print("- Scissors beats Paper")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYour choice: {player_choice}")
        print(f"Computer's choice: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(f"\nResult: {result}")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("\nThanks for playing!")
if __name__ == "__main__":
    play_game()