def read_players(filename='players.csv'):
    players = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                first_name, last_name, position, at_bats, hits = line.strip().split(',')
                players.append([first_name, last_name, position, int(at_bats), int(hits)])
    except FileNotFoundError:
        print("Player data file not found.")
    except Exception as e:
        print(f"An error occurred while reading the player data: {e}")
    return players

def write_players(players, filename='players.csv'):
    try:
        with open(filename, 'w') as file:
            for player in players:
                file.write(','.join(map(str, player)) + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the player data file: {e}")