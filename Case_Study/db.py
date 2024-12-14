import csv

FILENAME = "players.csv"

def read_players():
    try:
        players = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                # Convert `at_bats` and `hits` to integers
                row[2] = int(row[2])  
                row[3] = int(row[3])
                players.append(row)
        return players
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist


def write_players(players):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(players)
