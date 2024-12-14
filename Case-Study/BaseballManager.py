from datetime import date

class BaseballManager:
    FILENAME = "players.csv"

    def __init__(self):
        self.team = Team()
        self.team.players = FileHandler.load_players(self.FILENAME)

    def display_menu(self):
        print("=" * 64)
        print(f"Baseball Team Manager\n\nCURRENT DATE: {date.today()}")
        print("GAME DATE:    2021-03-21\nDAYS UNTIL GAME: 2")
        print("\nMENU OPTIONS")
        print("1 – Display lineup")
        print("2 – Add player")
        print("3 – Remove player")
        print("4 – Move player")
        print("5 – Edit player position")
        print("6 – Edit player stats")
        print("7 - Exit program")
        print("=" * 64)

    def add_player(self):
        first_name = input("First name: ")
        last_name = input("Last name: ")
        while True:
            position = input("Position: ").upper()
            if Player.is_valid_position(position):
                break
            print("Invalid position.")
        at_bats = int(input("At bats: "))
        hits = int(input("Hits: "))
        self.team.add_player(Player(first_name, last_name, position, at_bats, hits))

    def main_loop(self):
        while True:
            self.display_menu()
            option = input("Menu option: ")
            if option == "1":
                self.team.display_lineup()
            elif option == "2":
                self.add_player()
            elif option == "3":
                index = int(input("Lineup number to remove: "))
                self.team.remove_player(index)
            elif option == "4":
                current = int(input("Current lineup number: "))
                new = int(input("New lineup number: "))
                self.team.move_player(current, new)
            elif option == "5":
                index = int(input("Lineup number: "))
                new_position = input("New position: ").upper()
                self.team.edit_position(index, new_position)
            elif option == "6":
                index = int(input("Lineup number: "))
                new_at_bats = int(input("New at-bats: "))
                new_hits = int(input("New hits: "))
                self.team.edit_stats(index, new_at_bats, new_hits)
            elif option == "7":
                FileHandler.save_players(self.FILENAME, self.team.players)
                print("Bye!")
                break
            else:
                print("Invalid menu option.")