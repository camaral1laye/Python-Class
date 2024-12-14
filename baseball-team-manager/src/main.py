# FILE: /baseball-team-manager/baseball-team-manager/src/main.py

from ui import display_menu, display_lineup, get_user_option
from db import read_players
from lineup import Lineup

def main():
    lineup = Lineup(read_players())
    while True:
        display_menu()
        option = get_user_option()
        if option == "1":
            display_lineup(lineup)
        elif option == "2":
            lineup.edit_player_stats()
        elif option == "3":
            lineup.add_player()
        elif option == "4":
            lineup.remove_player()
        elif option == "5":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()