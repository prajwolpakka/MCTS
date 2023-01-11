from mcts import MCTS
from state import State

init_state = State([0, 0, 0, 0, 0, 0, 0, 0, 0])
print("Initial Board State:", init_state)
mcts = MCTS(search_limit=5000)

action, final_state = mcts.search(init_state)

print("Final State:", final_state)
