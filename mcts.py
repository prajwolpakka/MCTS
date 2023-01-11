import math
from node import Node
from copy import deepcopy
import random
from plays import random_play


class MCTS:
    def __init__(self, search_limit):
        self.search_limit = search_limit

    def search(self, init_state):
        self.root = Node(init_state)
        for _ in range(self.search_limit):
            node = self.select(self.root)
            reward = self.rollout(node.state)
            self.backpropogate(node, reward)

        best_node = self.get_best_node(self.root, 0)

        for action, node in self.root.children.items():
            if node == best_node:
                return action, node.state

    # select most promising node
    def select(self, node):
        while not node.isTerminal:
            if node.isFullyExpanded:
                node = self.get_best_node(node, math.sqrt(2))
                return node
            else:
                return self.expand(node)
        return node

    def expand(self, node):
        actions = node.state.getPossibleActions()
        for action in actions:
            if action not in node.children:
                newNode = Node(node.state.takeAction(action), node)
                node.children[action] = newNode
                if len(actions) == len(node.children):
                    node.isFullyExpanded = True
                return newNode
        raise Exception("Should never reach here")

    def rollout(self, state):
        score = random_play(state)
        return score

    # backpropagate the number of visits and score up to the root node
    def backpropogate(self, node, reward):
        # update nodes's up to root node
        while node is not None:
            node.visits += 1
            node.score += reward
            node = node.parent

    # select the best node basing on UCB1 formula
    def get_best_node(self, node, exploration_constant):
        # define best score & best moves
        best_score = float("-inf")
        best_moves = []

        # loop over child nodes
        for child_node in node.children.values():
            # get move score using UCT formula
            move_score = child_node.score / child_node.visits + exploration_constant * math.sqrt(
                math.log2(node.visits / child_node.visits)
            )

            # better move has been found
            if move_score > best_score:
                best_score = move_score
                best_moves = [child_node]

            # found as good move as already available
            elif move_score == best_score:
                best_moves.append(child_node)

        # return one of the best moves randomly
        return random.choice(best_moves)
