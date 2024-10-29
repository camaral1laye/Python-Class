# Define a dictionary of dictionaries to store player stats
game_stats = {
    "Elizabeth": {"Wins": 41, "Losses": 3, "Ties": 22},
    "Joel": {"Wins": 32, "Losses": 14, "Ties": 17},
    "Mike": {"Wins": 8, "Losses": 19, "Ties": 11}
}

def display_player_stats(player_name):
    """Display the stats for a given player name."""
    # Convert player_name to title case to handle case-insensitivity
    player_name = player_name.title()
    if player_name in game_stats:
        print("Wins:   ", game_stats[player_name]["Wins"])
        print("Losses: ", game_stats[player_name]["Losses"])
        print("Ties:   ", game_stats[player_name]["Ties"])
    else:
        print(f"There is no player named {player_name}.")

def main():
    """Main program loop for viewing player stats."""
    print("Game Stats Program")
    # Display all player names alphabetically
    print("ALL PLAYERS:")
    for player in sorted(game_stats):
        print(player)
    
    while True:
        # Prompt user for a player name
        player_name = input("\nEnter a player name: ")
        display_player_stats(player_name)
        
        # Ask user if they want to continue
        cont = input("Continue? (y/n): ").strip().lower()
        if cont != "y":
            print("Bye!")
            break

# Run the program
if __name__ == "__main__":
    main()