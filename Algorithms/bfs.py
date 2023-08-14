import time
from src.sokoban import *

def bfs():

    game = Sokoban("../Boards/board2.txt")

    game_queue = [game]     # Va a acutar como una cola. Meto al final pero saco del principio
    seen_states = set()

    start_time = time.time()


    nodesExpanded = 0
    solution_exists = 1

    while not game.victory():

        if len(game_queue) == 0:
            solution_exists = 0
            break
        game = game_queue.pop(0)   # dequeue

        valid_moves = game.get_valid_moves()

        for elem in valid_moves:
            alt_game = copy.deepcopy(game)
            alt_game.move(elem)
            nodesExpanded += 1

            _hash = hash(alt_game)

            # Evitamos expandir estados que ya vimos. Estamos asegurados de no eliminar un buen camino
            # posible dado que usamos BFS (que siempre expande los nodos con menor altura)

            if _hash not in seen_states:
                seen_states.add(_hash)
                game_queue.append(alt_game)  # enqueue


    end_time = time.time()

    return end_time, start_time, solution_exists, game, nodesExpanded, game_queue

# end_time, start_time, solution_exists, game, nodesExpanded, game_queue = bfs()
#
# print(f"\n{end_time - start_time}s taken")
# if solution_exists:
#     print(f"{len(game.moves)} moves done in best solution")
#     print(f"Expanded {nodesExpanded} nodes")
#     print(f"{len(game_queue)} nodes left on the frontier")
#     print(game.moves)
# else:
#     print("No solution was found")

