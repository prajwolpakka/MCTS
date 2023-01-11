class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.isTerminal = state.isTerminal()
        self.isFullyExpanded = self.isTerminal
        self.parent = parent
        self.visits = 0
        self.score = 0
        self.children = {}
