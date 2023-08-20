import time
from src.sokoban import *


def bfs(board, heuristic = None):

    game = Sokoban(board)

    game_queue = [game]     # Va a acutar como una cola. Meto al final pero saco del principio
    seen_states = set()

    seen_states.add(hash(game))

    start_time = time.time()

    nodesExpanded = 0
    solution_exists = 1

    while not game.victory():

        if len(game_queue) == 0:
            solution_exists = 0
            break
        game = game_queue.pop(0)   # dequeue
        nodesExpanded += 1

        for elem in game.get_valid_moves():
            alt_game = copy.deepcopy(game)
            alt_game.move(elem)

            _hash = hash(alt_game)

            # Evitamos expandir estados que ya vimos. Estamos asegurados de no eliminar un buen camino
            # posible dado que usamos BFS (que siempre expande los nodos con menor altura)

            if _hash not in seen_states:
                seen_states.add(_hash)
                game_queue.append(alt_game)  # enqueue

    end_time = time.time()

    return end_time, start_time, solution_exists, game, nodesExpanded, len(game_queue)


