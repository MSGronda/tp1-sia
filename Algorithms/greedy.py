import time

from sortedcontainers import SortedList

from src.GreedyBoard import GreedyBoard
from src.BoardTree import *


def greedy(board, heuristicStrategy):
    GreedyBoard.calculate_heuristic_strategy = heuristicStrategy
    game = GreedyBoard(board)

    start = time.time()

    stack = [game]
    visited_states = set()

    visited_states.add(hash(game))

    while stack and not game.victory():
        game = stack.pop()

        children = SortedList()

        for move in game.get_valid_moves():
            alt_game = copy.deepcopy(game)
            alt_game.move(move)

            _hash = hash(alt_game)

            if _hash not in visited_states:
                children.add(alt_game)
                visited_states.add(_hash)

        stack.extend(children)

    end = time.time()

    return end, start, game

# = = = = = Version anterior = = = = = =

# def greedy(board, heuristicStrategy):
#     game = Sokoban(board)
#     print("running")
#     BoardTreeNode.heuristicStrategy = heuristicStrategy #seteo la heuristica
#     mainNode = BoardTreeNode(game)
#
#     start = time.time()
#
#     result = mainNode.iterative_expand() #version iterativa
#     end = time.time()
#     return end, start, result

