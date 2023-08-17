from Algorithms.Heuristics.lost_game import lost_game_heuristic
from Algorithms.Heuristics.manhattan_distance import calculate_manhattan_distance

def combined_heuristic(game):
    return lost_game_heuristic(game) + calculate_manhattan_distance(game)