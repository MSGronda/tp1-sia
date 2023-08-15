import copy

from Algorithms.Heuristics.average_distance import calculate_average_distance
from Algorithms.Heuristics.euclidian_distance import calculate_euclidian_distance
from Algorithms.Heuristics.manhattan_distance import calculate_manhattan_distance
from src.sokoban import Sokoban


class AStarBoard(Sokoban):
    def __init__(self, path):
        super().__init__(path)
        self.heuristic = None

    def __deepcopy__(self, memo={}):

        board_copy = copy.copy(self.board)

        _copy = AStarBoard(None)
        _copy.build(board_copy, self.moves, self.player, self.boxes, self.goals, self.points)

        return _copy

    def __eq__(self, other):
        if isinstance(other, AStarBoard):
            return self.player == other.player and self.boxes == other.boxes
        return NotImplemented

    def __hash__(self):
        # TODO: posiblemente ineficiente usar el .tostring() (?)
        # Lo tengo que usar pq numpy no tiene hash para el ndarray
        return hash(str(self.player) + str(self.boxes))


    def __lt__(self, other):
        if self.heuristic is None:
            self.heuristic = calculate_manhattan_distance(self)
        if other.heuristic is None:
            other.heuristic = calculate_manhattan_distance(other)

        return self.heuristic + len(self.moves) < other.heuristic + len(other.moves)
