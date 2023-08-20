import time
from src.sokoban import *


def dfs(board, heuristic=None):
    game = Sokoban(board)

    game_stack = [game]  # Va a actuar como un stack. Si pongo al final y saco del final => es lo mismo que un stack
    seen_states = set()

    seen_states.add(hash(game))

    nodesExpanded = 0
    start_time = time.time()

    solution_exists = 1

    while not game.victory():
        if len(game_stack) == 0:
            solution_exists = 0
            break
        game = game_stack.pop()  # Obtengo el ultimo elemento
        nodesExpanded += 1

        for elem in game.get_valid_moves():
            alt_game = copy.deepcopy(game)
            alt_game.move(elem)

            # TODO: no se si es correcto eliminar repetidos en este caso
            _hash = hash(alt_game)

            # Evitamos expandir estados que ya vimos
            if _hash not in seen_states:
                seen_states.add(_hash)
                game_stack.append(alt_game)  # Pongo al final de la lista

    end_time = time.time()
    return end_time, start_time, solution_exists, game, nodesExpanded, len(game_stack)
