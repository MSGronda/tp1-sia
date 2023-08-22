from collections import deque
from puzzle_game.game_with_heuristic import GameWithHeuristic
from puzzle_game.algorithms.a_star import *
from puzzle_game.algorithms.bfs import *
from puzzle_game.algorithms.dfs import *
from puzzle_game.heuristics.manhattan_distance import *
from puzzle_game.heuristics.incorrect_numbers import *


def gameSolver(boardToSolve, algorithmToUse, heuristicToUse):
    match heuristicToUse:
        case "manhattan":
            heuristic = get_total_manhattan
        case "incorrect_numbers":
            heuristic = get_sum_incorrect
        case _:
            print("The heuristic is incorrect")
            exit()

    match algorithmToUse:
        case "bfs":
            add_to_process = bfs_add
        case "dfs":
            add_to_process = dfs_add
        case "a_star":
            add_to_process = a_star_add
        case _:
            print("The algorithm entered is invalid")
            exit()

    game_first_instance = GameWithHeuristic(boardToSolve, heuristic)
    gamesToProcess = deque([game_first_instance])
    alreadyChecked = set()
    steps = 0
    casesAvoid = 0

    while len(gamesToProcess) > 0:
        game = gamesToProcess.popleft()
        steps += 1

        alreadyChecked.add(hash(game))

        if game.is_solved():
            return steps, game.depth

        possible_moves = game.get_possible_moves()
        for move in possible_moves:
            if game.can_move(move):
                new_game = game.get_new_game_by_move(move)
                if hash(new_game) not in alreadyChecked:
                    add_to_process(gamesToProcess, new_game)  # insert in a sorted way
                else:
                    casesAvoid += 1

    print(f"Game couldn't be solved, cases avoided = {casesAvoid}, checked cases = {steps}")
    return None
