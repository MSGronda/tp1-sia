import copy

from src.sokoban import Sokoban
import time


def iddfs() -> Sokoban | None:
    board = "../Boards/board3.txt"
    max_depth = 1000
    for depth_limit in range(0, max_depth + 1, 4):
        game = Sokoban(board)
        stack = [game]
        visited = set()
        while stack:
            game = stack.pop()
            if len(game.moves) <= depth_limit:
                if game.victory():
                    return game
                visited.add(hash(game))
                for move in game.get_valid_moves():
                    alt_game = copy.deepcopy(game)
                    alt_game.move(move)
                    if hash(alt_game) not in visited:
                        stack.append(alt_game)
    return None


start = time.time()
result = iddfs()
print(result.moves if result else "No solution was found")
end = time.time()
print(f"it took {end - start} seconds to resolve this")
