import copy
from sortedcontainers import SortedList
import time
from src.AStarBoard import AStarBoard

def a_star(board,heuristicStrategy):
    AStarBoard.calculate_heuristic_strategy = heuristicStrategy
    game = AStarBoard(board)

    game_queue = SortedList([game])  # Usamos una lista orderada (la frontera del arbol)
    seen_states = set()

    seen_states.add(hash(game))

    start_time = time.time()

    nodesExpanded = 0
    solution_exists = 1

    while not game.victory():

        if len(game_queue) == 0:
            solution_exists = 0
            break

        game = game_queue.pop(0)

        for elem in game.get_valid_moves():
            alt_game = copy.deepcopy(game)
            alt_game.move(elem)
            nodesExpanded += 1

            _hash = hash(alt_game)

            if _hash not in seen_states:
                seen_states.add(_hash)
                game_queue.add(alt_game)

    end_time = time.time()
    return end_time, start_time, solution_exists, game, nodesExpanded, game_queue


