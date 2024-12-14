import db

# Tuple of valid positions
VALID_POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

def display_menu():
    print("=" * 50)
    print("                Baseball Team Manager")
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print("=" * 50)

def display_lineup(lineup):
    print("Player           POS   AB     H     AVG")
    print("-" * 50)
    for i, player in enumerate(lineup, start=1):
        name, position, at_bats, hits = player
        avg = calculate_batting_average(hits, at_bats)
        print(f"{i:2} {name:15} {position:3} {at_bats:5} {hits:5} {avg:6.3f}")

def calculate_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0.0
    return round(hits / at_bats, 3)

def add_player(lineup):
    name = input("Name: ")
    while True:
        position = input("Position: ").upper()
        if position in VALID_POSITIONS:
            break
        else:
            print(f"Invalid position. Valid positions are: {', '.join(VALID_POSITIONS)}")
    try:
        at_bats = int(input("At bats: "))
        hits = int(input("Hits: "))
        if at_bats < 0 or hits < 0 or hits > at_bats:
            print("Invalid stats. Hits cannot be greater than at bats, and numbers must be non-negative.")
            return
        lineup.append([name, position, at_bats, hits])
        print(f"{name} was added to the lineup.")
    except ValueError:
        print("Invalid input. Please enter valid integers for at-bats and hits.")

def remove_player(lineup):
    try:
        number = int(input("Lineup number to remove: "))
        if 1 <= number <= len(lineup):
            removed_player = lineup.pop(number - 1)
            print(f"{removed_player[0]} was removed.")
        else:
            print("Invalid lineup number.")
    except ValueError:
        print("Invalid input. Please enter a valid lineup number.")

def move_player(lineup):
    try:
        current_number = int(input("Current lineup number: "))
        if 1 <= current_number <= len(lineup):
            player = lineup.pop(current_number - 1)
            new_number = int(input("New lineup number: "))
            lineup.insert(new_number - 1, player)
            print(f"{player[0]} was moved.")
        else:
            print("Invalid lineup number.")
    except ValueError:
        print("Invalid input. Please enter valid lineup numbers.")

def edit_player_position(lineup):
    try:
        number = int(input("Lineup number: "))
        if 1 <= number <= len(lineup):
            player = lineup[number - 1]
            while True:
                new_position = input(f"You selected {player[0]} (POS={player[1]}). New Position: ").upper()
                if new_position in VALID_POSITIONS:
                    player[1] = new_position
                    print(f"{player[0]}'s position was updated.")
                    break
                else:
                    print(f"Invalid position. Valid positions are: {', '.join(VALID_POSITIONS)}")
        else:
            print("Invalid lineup number.")
    except ValueError:
        print("Invalid input. Please enter a valid lineup number.")

def edit_player_stats(lineup):
    try:
        number = int(input("Lineup number: "))
        if 1 <= number <= len(lineup):
            player = lineup[number - 1]
            try:
                new_at_bats = int(input(f"Current at-bats: {player[2]}. New at-bats: "))
                new_hits = int(input(f"Current hits: {player[3]}. New hits: "))
                if new_at_bats < 0 or new_hits < 0 or new_hits > new_at_bats:
                    print("Invalid stats. Hits cannot be greater than at bats, and numbers must be non-negative.")
                    return
                player[2] = new_at_bats
                player[3] = new_hits
                print(f"{player[0]}'s stats were updated.")
            except ValueError:
                print("Invalid input. Please enter valid integers for at-bats and hits.")
        else:
            print("Invalid lineup number.")
    except ValueError:
        print("Invalid input. Please enter a valid lineup number.")

def main():
    lineup = db.read_players()
    while True:
        display_menu()
        option = input("Menu option: ").strip()
        if option == "1":
            display_lineup(lineup)
        elif option == "2":
            add_player(lineup)
        elif option == "3":
            remove_player(lineup)
        elif option == "4":
            move_player(lineup)
        elif option == "5":
            edit_player_position(lineup)
        elif option == "6":
            edit_player_stats(lineup)
        elif option == "7":
            db.write_players(lineup)
            print("Bye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()