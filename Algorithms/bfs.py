import time
from src.sokoban import *

game = Sokoban("../Boards/board.txt")

game_queue = [game]     # Va a acutar como una cola. Meto al final pero saco del principio
seen_states = set()

start_time = time.time()

while not game.victory():

    game = game_queue.pop(0)   # dequeue

    valid_moves = game.get_valid_moves()

    for elem in valid_moves:
        alt_game = copy.deepcopy(game)
        alt_game.move(elem)

        _hash = hash(alt_game)

        # Evitamos expandir estados que ya vimos
        if _hash not in seen_states:
            seen_states.add(_hash)
            game_queue.append(alt_game)  # enqueue


end_time = time.time()

print(f"\n{end_time - start_time}s taken")
print(f"{len(game.moves)} moves done in best solution")
print(game.moves)

