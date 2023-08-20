from puzzle_game.game import Game
from puzzle_game.utils.coordinates import Directions
from collections import deque

game_first_instance = Game("./boards/easy5")
gamesToProcess = deque([game_first_instance])
alreadyChecked = set()
steps = 0
casesAvoid = 0

while len(gamesToProcess) > 0:
    game = gamesToProcess.popleft()
    steps += 1

    alreadyChecked.add(hash(game))

    if game.is_solved():
        print(f"Game is solved! All it took was {steps} steps")
        exit()

    for direction in Directions:
        if game.can_move(direction):
            new_game = game.get_new_game_by_move(direction)
            if hash(new_game) not in alreadyChecked:
                gamesToProcess.append(new_game)
            else:
                casesAvoid += 1

print(f"Game couldn't be solved, cases avoided = {casesAvoid}, checked cases = {steps}")
