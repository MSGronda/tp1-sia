from src.sokoban import *


class BoardTreeNode:
    visitedStates = set()

    def __init__(self, board: Sokoban):
        self.board = board
        self.children: list[tuple[int, BoardTreeNode, Moves]] = []

    def expand(self) -> bool:
        # creo un nodo hijo por cada movimiento
        if self.board.victory():
            print("Solution found")
            print(self.board.moves)
            return True

        BoardTreeNode.visitedStates.add(hash(self.board))

        for move in self.board.get_valid_moves():
            alt_game = copy.deepcopy(self.board)
            alt_game.move(move)

            if hash(alt_game) not in BoardTreeNode.visitedStates:
                game_node = BoardTreeNode(alt_game)
                current_distance = alt_game.calculate_manhattan_distance()
                self.children.append((current_distance, game_node, move))

        self.children.sort(key=lambda item: item[0])

        for _, childNode, _ in self.children:
            if childNode.expand():
                return True

        return False
