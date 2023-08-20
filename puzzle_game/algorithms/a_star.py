from puzzle_game.a_star_game import A_Star_Game
from collections import deque
from bisect import insort

game_first_instance = A_Star_Game("../boards/difficult", 0)
gamesToProcess = deque([game_first_instance])
alreadyChecked = set()
steps = 0
casesAvoid = 0

while len(gamesToProcess) > 0:
    game = gamesToProcess.popleft()
    print(game)
    steps += 1

    alreadyChecked.add(hash(game))

    if game.is_solved():
        print(f"Game is solved! All it took was {steps} steps")
        print(f"The depth of the answer is {game.depth}")
        exit()

    possible_moves = game.get_possible_moves()
    for move in possible_moves:
        if game.can_move(move):
            new_game = game.get_new_game_by_move(move)
            if hash(new_game) not in alreadyChecked:
                insort(gamesToProcess, new_game)  # insert in a sorted way
            else:
                casesAvoid += 1

print(f"Game couldn't be solved, cases avoided = {casesAvoid}, checked cases = {steps}")
