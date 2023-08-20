from puzzle_game.game import Game
from puzzle_game.heuristics.manhattan_distance import get_total_manhattan


class A_Star_Game(Game):
    def __init__(self, pathToBoard, depth):
        super().__init__(pathToBoard, depth)

    def __lt__(self, other):
        self_cost = get_total_manhattan(self.board) + self.depth
        other_cost = get_total_manhattan(other.board) + other.depth
        return self_cost < other_cost
