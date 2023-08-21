from puzzle_game.game import Game


class GameWithHeuristic(Game):
    def __init__(self, pathToBoard, heuristic):
        super().__init__(pathToBoard)
        self.heuristic = heuristic

    def __lt__(self, other):
        self_cost = self.heuristic(self.board) + self.depth
        other_cost = self.heuristic(other.board) + other.depth
        return self_cost < other_cost
