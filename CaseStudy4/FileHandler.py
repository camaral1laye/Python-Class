import csv

class FileHandler:
    @staticmethod
    def load_players(filename):
        players = []
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    players.append(Player(row[0], row[1], row[2], int(row[3]), int(row[4])))
        except FileNotFoundError:
            print("No existing data file found. Starting fresh.")
        return players

    @staticmethod
    def save_players(filename, players):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for player in players:
                writer.writerow([player.first_name, player.last_name, player.position, player.at_bats, player.hits])