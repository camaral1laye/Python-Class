def display_menu():
    print("Menu:")
    print("1. Display Lineup")
    print("2. Edit Player Stats")
    print("3. Add Player")
    print("4. Remove Player")
    print("5. Exit")

def display_lineup(lineup):
    print("Current Lineup:")
    for index, player in enumerate(lineup, start=1):
        print(f"{index}. {player.full_name()} - Position: {player.position}, At Bats: {player.at_bats}, Hits: {player.hits}")

def get_user_input(prompt):
    return input(prompt).strip()