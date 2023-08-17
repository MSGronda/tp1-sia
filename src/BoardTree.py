from __future__ import annotations

import queue

from Algorithms.Heuristics.manhattan_distance import calculate_manhattan_distance
from src.sokoban import *


class BoardTreeNode:
    visitedStates = set()
    heuristicStrategy = None # a inicializar con el puntero a funcion correspondiente
    def __init__(self, board: Sokoban):
        self.board = board
        self.children: list[tuple[int, BoardTreeNode, Moves]] = []
        if BoardTreeNode.heuristicStrategy is None:
            raise ValueError("Please initialize the desired heuristic as a class variable")

    def expand(self) -> Sokoban | None:
        # creo un nodo hijo por cada movimiento
        if self.board.victory():
            return self.board

        BoardTreeNode.visitedStates.add(hash(self.board))

        for move in self.board.get_valid_moves():
            alt_game = copy.deepcopy(self.board)
            alt_game.move(move)

            if hash(alt_game) not in BoardTreeNode.visitedStates:
                game_node = BoardTreeNode(alt_game)
                current_distance = BoardTreeNode.heuristicStrategy(alt_game)
                self.children.append((current_distance, game_node, move))

        self.children.sort(key=lambda item: item[0])

        for _, childNode, _ in self.children:
            result = childNode.expand()
            if result:
                return result

        return None

    def iterative_expand(self) -> Sokoban | None:
        visited_states = set()
        stack = [self]

        while stack:
            node = stack.pop()

            if node.board.victory():
                return node.board

            if hash(node.board) not in visited_states:
                visited_states.add(hash(node.board))

                for move in node.board.get_valid_moves():
                    alt_game = copy.deepcopy(node.board)
                    alt_game.move(move)

                    if hash(alt_game) not in visited_states:
                        game_node = BoardTreeNode(alt_game)
                        current_distance = BoardTreeNode.heuristicStrategy(alt_game)
                        node.children.append((current_distance, game_node, move))

                node.children.sort(key=lambda item: item[0])
                for _, childNode, _ in reversed(node.children):
                    stack.append(childNode)

        return None
