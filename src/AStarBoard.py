import copy

from Algorithms.Heuristics.manhattan_distance import calculate_manhattan_distance
from src.sokoban import Sokoban

class AStarBoard(Sokoban):
    def __init__(self, path):
        super().__init__(path)
        self.manhattan_distance = None

    def __deepcopy__(self, memo={}):

        board_copy = copy.copy(self.board)

        _copy = AStarBoard(None)
        _copy.build(board_copy, self.moves, self.player, self.boxes, self.goals, self.points)

        return _copy

    def __lt__(self, other):
        if self.manhattan_distance is None:
            self.manhattan_distance = calculate_manhattan_distance(self)
        if other.manhattan_distance is None:
            other.manhattan_distance = calculate_manhattan_distance(other)

        return self.manhattan_distance + len(self.moves) < other.manhattan_distance + len(other.moves)


