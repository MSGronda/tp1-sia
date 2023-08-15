import copy
from sortedcontainers import SortedList
import time
from src.AStarBoard import AStarBoard

game = AStarBoard("../Boards/board.txt")

game_queue = SortedList([game])  # Usamos una lista orderada (la frontera del arbol)
seen_states = set()

start_time = time.time()


nodesExpanded = 0
solution_exists = 1

while not game.victory():
    if len(game_queue) == 0:
        solution_exists = 0
        break

    game = game_queue.pop(0)

    valid_moves = game.get_valid_moves()

    for elem in valid_moves:
        alt_game = copy.deepcopy(game)
        alt_game.move(elem)
        nodesExpanded += 1

        _hash = hash(alt_game)

        if _hash not in seen_states:
            seen_states.add(_hash)
            game_queue.add(alt_game)


end_time = time.time()

print(f"\n{end_time - start_time}s taken")
if solution_exists:
    print(f"{len(game.moves)} moves done in best solution")
    print(f"Expanded {nodesExpanded} nodes")
    print(f"{len(game_queue)} nodes left on the frontier")
    print(game.moves)
else:
    print("No solution was found")

