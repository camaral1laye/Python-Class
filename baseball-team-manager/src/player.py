class Player:
    def __init__(self, first_name, last_name, position, at_bats=0, hits=0):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def batting_average(self):
        if self.at_bats > 0:
            return self.hits / self.at_bats
        return 0.0