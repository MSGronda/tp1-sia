import copy

from Algorithms.Heuristics.average_distance import calculate_average_distance
from Algorithms.Heuristics.euclidian_distance import calculate_euclidian_distance
from Algorithms.Heuristics.manhattan_distance import calculate_manhattan_distance
from src.sokoban import Sokoban


class GreedyBoard(Sokoban):
    calculate_heuristic_strategy = None  # variable de clase que tiene puntero a funcion de heuristica

    def __init__(self, path):
        super().__init__(path)
        self.heuristic = None
        if GreedyBoard.calculate_heuristic_strategy is None:
            raise ValueError("heuristic strategy must be initialized as a class variable")

    def __deepcopy__(self, memo=None):
        _copy = GreedyBoard(None)
        _copy.build(self.board, self.moves, self.player, self.boxes, self.goals, self.points)
        return _copy

    def __lt__(self, other):
        if self.heuristic is None:
            self.heuristic = GreedyBoard.calculate_heuristic_strategy(self)
        if other.heuristic is None:
            other.heuristic = GreedyBoard.calculate_heuristic_strategy(other)

        return self.heuristic < other.heuristic
