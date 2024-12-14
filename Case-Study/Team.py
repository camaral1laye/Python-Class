class Team:
    def __init__(self):
        self.players = []

    def display_lineup(self):
        print("   Player                             POS       AB     H     AVG")
        print("----------------------------------------------------------------")
        for index, player in enumerate(self.players, start=1):
            print(player.display(index))

    def add_player(self, player):
        self.players.append(player)
        print(f"{player.full_name} was added.")

    def remove_player(self, index):
        if 1 <= index <= len(self.players):
            removed = self.players.pop(index - 1)
            print(f"{removed.full_name} was removed.")
        else:
            print("Invalid lineup number.")

    def move_player(self, current_index, new_index):
        if 1 <= current_index <= len(self.players) and 1 <= new_index <= len(self.players):
            player = self.players.pop(current_index - 1)
            self.players.insert(new_index - 1, player)
            print(f"{player.full_name} was moved.")
        else:
            print("Invalid lineup numbers.")

    def edit_position(self, index, new_position):
        if 1 <= index <= len(self.players) and Player.is_valid_position(new_position):
            self.players[index - 1].position = new_position
            print(f"{self.players[index - 1].full_name}'s position was updated.")
        else:
            print("Invalid position or lineup number.")

    def edit_stats(self, index, new_at_bats, new_hits):
        if 1 <= index <= len(self.players) and 0 <= new_hits <= new_at_bats:
            self.players[index - 1].at_bats = new_at_bats
            self.players[index - 1].hits = new_hits
            print(f"{self.players[index - 1].full_name}'s stats were updated.")
        else:
            print("Invalid stats or lineup number.")
