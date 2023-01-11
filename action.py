class Action:
    def __init__(self, player, idx):
        self.player = player
        self.idx = idx

    def __str__(self):
        return str((self.idx))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.idx == other.idx and self.player == other.player

    def __hash__(self):
        return hash((self.idx, self.player))
