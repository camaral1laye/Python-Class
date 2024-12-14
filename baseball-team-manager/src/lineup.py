class Lineup:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def move_player(self, old_index, new_index):
        if 0 <= old_index < len(self.players) and 0 <= new_index < len(self.players):
            player = self.players.pop(old_index)
            self.players.insert(new_index, player)

    def get_player(self, index):
        if 0 <= index < len(self.players):
            return self.players[index]
        return None

    def edit_player(self, index, at_bats, hits):
        if 0 <= index < len(self.players):
            player = self.players[index]
            player.at_bats = at_bats
            player.hits = hits

    def number_of_players(self):
        return len(self.players)

    def __iter__(self):
        return iter(self.players)