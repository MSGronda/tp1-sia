from puzzle_game.game import Game
from puzzle_game.coordinates import Directions
from collections import deque

game_first_instance = Game("./boards/easy3")
gamesToProcess = deque([game_first_instance])
alreadyChecked = set()
steps = 0

while len(gamesToProcess) > 0:
    game = gamesToProcess.popleft()
    steps += 1

    if hash(game) in alreadyChecked:
        continue

    alreadyChecked.add(hash(game))

    if game.is_solved():
        print(f"Game is solved! All it took was {steps} steps")
        exit()

    for direction in Directions:
        if game.can_move(direction):
            gamesToProcess.append(game.get_new_game_by_move(direction))

print("Game couldn't be solved")
