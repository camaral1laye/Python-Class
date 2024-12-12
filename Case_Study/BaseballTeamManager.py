class Player:
    def __init__(self, name, position, at_bats, hits):
        self.name = name
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

    def batting_average(self):
        return round(self.hits / self.at_bats, 3) if self.at_bats > 0 else 0.0

    def __str__(self):
        return f"{self.name:15} {self.position:5} {self.at_bats:6} {self.hits:6} {self.batting_average():6}"


def display_menu():
    print("=" * 64)
    print("Baseball Team Manager")
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print("=" * 64)


def display_lineup(lineup):
    print("Player           POS   AB     H     AVG")
    print("-" * 64)
    for i, player in enumerate(lineup, start=1):
        print(f"{i:2} {player}")


def add_player(lineup):
    try:
        name = input("Name: ")
        position = input("Position: ")
        at_bats = int(input("At bats: "))
        hits = int(input("Hits: "))
        lineup.append(Player(name, position, at_bats, hits))
        print(f"{name} was added.")
    except ValueError:
        print("Invalid input. Please enter numeric values for at-bats and hits.")


def remove_player(lineup):
    try:
        number = int(input("Lineup number to remove: "))
        if 1 <= number <= len(lineup):
            removed_player = lineup.pop(number - 1)
            print(f"{removed_player.name} was removed.")
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
            print(f"{player.name} was moved.")
        else:
            print("Invalid lineup number.")
    except ValueError:
        print("Invalid input. Please enter valid lineup numbers.")


def edit_player_position(lineup):
    try:
        number = int(input("Lineup number: "))
        if 1 <= number <= len(lineup):
            player = lineup[number - 1]
            new_position = input(f"You selected {player.name} POS={player.position}. New Position: ")
            player.position = new_position
            print(f"{player.name}'s position was updated.")
        else:
            print("Invalid lineup number.")
    except ValueError:
        print("Invalid input. Please enter a valid lineup number.")


def edit_player_stats(lineup):
    try:
        number = int(input("Lineup number: "))
        if 1 <= number <= len(lineup):
            player = lineup[number - 1]
            new_at_bats = int(input(f"Current at-bats: {player.at_bats}. New at-bats: "))
            new_hits = int(input(f"Current hits: {player.hits}. New hits: "))
            player.at_bats = new_at_bats
            player.hits = new_hits
            print(f"{player.name}'s stats were updated.")
        else:
            print("Invalid lineup number.")
    except ValueError:
        print("Invalid input. Please enter numeric values for at-bats and hits.")


def main():
    lineup = []  # List to store Player objects

    while True:
        display_menu()
        try:
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
                print("Bye!")
                break
            else:
                print("Invalid option. Please try again.")
        except EOFError:
            print("Input error. Exiting program.")
            break


if __name__ == "__main__":
    main()