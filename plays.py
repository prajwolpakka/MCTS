import random


def random_play(state):
    # The winner should be the one who performed a move
    simulating_for = (2 - state.currentPlayer) + 1

    # until game is over
    while not state.isTerminal():
        action = random.choice(state.getPossibleActions())
        state = state.takeAction(action)

    # the one who performed last move
    last_player = action.player
    if state.won():
        return 1 if last_player == simulating_for else 0
    return 0.5
