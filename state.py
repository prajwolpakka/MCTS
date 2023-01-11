from copy import deepcopy
from action import Action


class State:
    def __init__(self, init_state):
        self.board = init_state
        self.currentPlayer = 1 if self.board.count(0) % 2 == 0 else 2

    def getCurrentPlayer(self):
        return self.currentPlayer

    def getPossibleActions(self):
        possibleActions = []
        for idx, data in enumerate(self.board):
            if data == 0:
                possibleActions.append(Action(player=self.currentPlayer, idx=idx))
        return possibleActions

    def takeAction(self, action):
        newState = deepcopy(self)  # creates clone of current state
        newState.board[action.idx] = action.player
        newState.currentPlayer = (self.currentPlayer + 2) % 2 + 1
        return newState

    def isTerminal(self):
        #  someone has won
        if self.won():
            return True

        # no position on board is remaining
        elif self.board.count(0) == 0:
            return True

        else:
            return False

    def won(self):
        # check rows
        for i in range(3):
            if self.board[0 + 3 * i] == self.board[1 + 3 * i] == self.board[2 + 3 * i] != 0:
                return True

        # check columns
        for i in range(3):
            if self.board[0 + i] == self.board[3 + i] == self.board[6 + i] != 0:
                return True

        # primary diagonal
        if self.board[0] == self.board[4] == self.board[8] != 0:
            return True

        # secondary diagonal
        if self.board[2] == self.board[4] == self.board[6] != 0:
            return True

        return False

    def __str__(self):
        repr = "\n"
        repr += f"{self.board[0]}|{self.board[1]}|{self.board[2]}\n"
        repr += f"{self.board[3]}|{self.board[4]}|{self.board[5]}\n"
        repr += f"{self.board[6]}|{self.board[7]}|{self.board[8]}\n"
        return repr
