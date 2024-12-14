class Player:
    VALID_POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.at_bats = at_bats
        self.hits = hits

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def batting_average(self):
        if self.at_bats == 0:
            return 0.0
        return round(self.hits / self.at_bats, 3)

    def display(self, index):
        return f"{index:2} {self.full_name:30} {self.position:3} {self.at_bats:7} {self.hits:7} {self.batting_average:7.3f}"

    @classmethod
    def is_valid_position(cls, position):
        return position.upper() in cls.VALID_POSITIONS