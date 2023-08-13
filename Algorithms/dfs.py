import time
from src.sokoban import *

game = Sokoban("../Boards/board2.txt")

game_stack = [game]  # Va a actuar como un stack. Si pongo al final y saco del final => es lo mismo que un stack
seen_states = set()

nodesExpanded = 0
start_time = time.time()

while not game.victory():
    game = game_stack.pop()     # Obtengo el ultimo elemento

    valid_moves = game.get_valid_moves()

    for elem in valid_moves:
        alt_game = copy.deepcopy(game)
        alt_game.move(elem)
        nodesExpanded += 1
        # TODO: no se si es correcto eliminar repetidos en este caso

        _hash = hash(alt_game)



        # Evitamos expandir estados que ya vimos
        if _hash not in seen_states:
            seen_states.add(_hash)
            game_stack.append(alt_game)     # Pongo al final de la lista

end_time = time.time()

print(f"\n{end_time - start_time}s taken")
print(f"{len(game.moves)} moves done")
print(f"expanded {nodesExpanded} nodes")
print(f"{len(game_stack)} nodes left on the frontier")
print(game.moves)
