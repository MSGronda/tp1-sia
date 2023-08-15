import copy
from enum import Enum
import numpy as np


class BoardItems(Enum):
    EMPTY_SPACE = ' '
    WALL = '#'
    BOX = '%'
    GOAL = '*'
    PLAYER = '$'
    GOAL_WITH_BOX = '@'
    GOAL_WITH_PLAYER = '&'


class Moves(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


MOVE_X = 1
MOVE_Y = 0

COORD_X = 0
COORD_Y = 1

ITEM_MAP = {
    ' ': BoardItems.EMPTY_SPACE,
    '#': BoardItems.WALL,
    '%': BoardItems.BOX,
    '*': BoardItems.GOAL,
    '$': BoardItems.PLAYER,
    '@': BoardItems.GOAL_WITH_BOX,
    '&': BoardItems.GOAL_WITH_PLAYER,
}


def generate_board(path):
    # TODO: chequeos de todo tipo

    matrix = []
    with open(path) as file:
        for i, line in enumerate(file):
            matrix.append([])
            for elem in line:

                # Vale la pena convertir el arreglo de chars al enum
                # para no tener que estar haciendo enum.value
                # Testeo: con chars 10.7s, con enum 7.8s para generar
                # 1000000 de movimientos.

                if elem in ITEM_MAP:
                    item = ITEM_MAP[elem]
                    matrix[i].append(item)

    return np.array(matrix)


class Sokoban:
    def __init__(self, path):

        # Al no tener polimorfismo y dado que tenemos que hacer
        # deepcopy del Sokoban, tengo que hacer esta maldad

        self.board = None
        self.width = None
        self.height = None

        self.moves = []

        self.player = None
        self.boxes = []
        self.goals = []

        self.points = 0

        if path is not None:
            # Matriz de n x m
            board = generate_board(path)
            self.build(board, [])

    # Sirve para cuando hagamos deepcopy
    def build(self, board, moves, player=[], boxes=[], goals=[], points=0):

        self.board = board
        self.moves = copy.deepcopy(moves)

        self.height, self.width = np.shape(self.board)

        # Por eficiencia, puedo direcatmente pasarle una copia de los locations
        # o lo puede calcular por su cuenta.
        if len(player) == 0 or len(boxes) == 0 or len(goals) == 0:
            self.locate_items()
        else:
            self.player = copy.deepcopy(player)
            self.boxes = copy.deepcopy(boxes)
            self.goals = copy.deepcopy(goals)
            self.points = points

    # METODOS "PRIVADOS"

    def locate_items(self):

        # Consigo la posicion de todos los elementos relevantes
        # para no tener que iterar constantemente

        for y, row in enumerate(self.board):
            for x, item in enumerate(row):

                if item == BoardItems.PLAYER:
                    self.player = [x, y]
                elif item == BoardItems.GOAL_WITH_PLAYER:
                    self.player = [x, y]
                    self.goals.append([x, y])
                elif item == BoardItems.BOX:
                    self.boxes.append([x, y])
                elif item == BoardItems.GOAL:
                    self.goals.append([x, y])
                elif item == BoardItems.GOAL_WITH_BOX:
                    self.boxes.append([x, y])
                    self.goals.append([x, y])

                    self.points += 1


    # METODOS "PUBLICOS"

    def get_valid_moves(self):
        valid_moves = []
        for move in Moves:
            if self.can_move(move):
                valid_moves.append(move)
        return valid_moves

    def can_move(self, move):
        # Esta dentro de la matriz
        if 0 <= self.player[COORD_X] + move.value[MOVE_X] < self.width and 0 <= self.player[COORD_Y] + move.value[MOVE_Y] < self.height:

            block = self.board[self.player[COORD_Y] + move.value[MOVE_Y], self.player[COORD_X] + move.value[MOVE_X]]

            # Caso: me muevo a un espacio vacio
            if block == BoardItems.EMPTY_SPACE or block == BoardItems.GOAL:
                return True

            # Caso: quiere mover una caja
            elif block == BoardItems.BOX or block == BoardItems.GOAL_WITH_BOX:

                # Me fijo que adonde quiero empujar la caja, es dentro de la matriz
                if 0 <= self.player[COORD_X] + move.value[MOVE_X] * 2 < self.width and 0 <= self.player[COORD_Y] + move.value[MOVE_Y] * 2 < self.height:

                    move_to_block = self.board[
                        self.player[COORD_Y] + move.value[MOVE_Y] * 2, self.player[COORD_X] + move.value[MOVE_X] * 2]

                    # Es valido adonde quiero mover la caja
                    if move_to_block == BoardItems.EMPTY_SPACE or move_to_block == BoardItems.GOAL:
                        return True
        return False

    def move(self, move):

        # TODO: eliminar por eficiencia (?)
        # Testeo: con if: 7.8s, sin if: 6.9s
        if not self.can_move(move):
            return

        # Agrego el movimiento a los moviemientos hechos
        self.moves.append(move)

        # Cambio la posicion anterior del jugador
        old_pos_block = self.board[self.player[COORD_Y], self.player[COORD_X]]

        if old_pos_block == BoardItems.PLAYER:
            self.board[self.player[COORD_Y], self.player[COORD_X]] = BoardItems.EMPTY_SPACE
        elif old_pos_block == BoardItems.GOAL_WITH_PLAYER:
            self.board[self.player[COORD_Y], self.player[COORD_X]] = BoardItems.GOAL

        # Cambio la nueva posicion del jugador
        self.player[COORD_X] += move.value[MOVE_X]
        self.player[COORD_Y] += move.value[MOVE_Y]

        new_pos_block = self.board[self.player[COORD_Y], self.player[COORD_X]]

        if new_pos_block == BoardItems.EMPTY_SPACE:
            self.board[self.player[COORD_Y], self.player[COORD_X]] = BoardItems.PLAYER
        elif new_pos_block == BoardItems.GOAL:
            self.board[self.player[COORD_Y], self.player[COORD_X]] = BoardItems.GOAL_WITH_PLAYER
        # Caso: quiero mover un caja
        elif new_pos_block == BoardItems.BOX or new_pos_block == BoardItems.GOAL_WITH_BOX:

            # Ahora el jugador esta donde estaba la caja
            if new_pos_block == BoardItems.BOX:
                self.board[self.player[COORD_Y], self.player[COORD_X]] = BoardItems.PLAYER
            else:
                # Desplace la caja de un goal
                self.board[self.player[COORD_Y], self.player[COORD_X]] = BoardItems.GOAL_WITH_PLAYER

                # La caja deja de estar encima de un goal => pierdo un punto
                self.points -= 1

            # = Muevo la caja a la nueva posicion =

            # Primero updateo la posicion que tenemos guardada aparte

            box_pos_idx = self.boxes.index([self.player[COORD_X], self.player[COORD_Y]]) # Adonde esta el jugador es donde solia estar la caja
            self.boxes[box_pos_idx] = [self.player[COORD_X] + move.value[MOVE_X], self.player[COORD_Y] + move.value[MOVE_Y]] # Updateo la posicion

            # Luego updateo la posicion en el board

            new_pos_box_block = self.board[self.player[COORD_Y] + move.value[MOVE_Y], self.player[COORD_X] + move.value[MOVE_X]]

            if new_pos_box_block == BoardItems.EMPTY_SPACE:
                self.board[self.player[COORD_Y] + move.value[MOVE_Y], self.player[COORD_X] + move.value[MOVE_X]] = BoardItems.BOX
            elif new_pos_box_block == BoardItems.GOAL:
                self.board[
                    self.player[COORD_Y] + move.value[MOVE_Y], self.player[COORD_X] + move.value[MOVE_X]] = BoardItems.GOAL_WITH_BOX

                # La caja esta encima de un goal => consigo un punto
                self.points += 1

    def get_points(self):
        return self.points

    def get_goal_count(self):
        return len(self.goals)

    def victory(self):
        return self.points == len(self.goals)

    def get_board(self):
        return self.board

    def get_goals(self):
        return self.goals

    def get_boxes(self):
        return self.boxes

    def __hash__(self):
        # TODO: posiblemente ineficiente usar el .tostring() (?)
        # Lo tengo que usar pq numpy no tiene hash para el ndarray
        return hash(self.board.tostring())

    def __eq__(self, other):
        if isinstance(other, Sokoban):
            return (self.board == other.board).all()
        return NotImplemented

    def __deepcopy__(self, memo={}):

        board_copy = copy.copy(self.board)

        _copy = Sokoban(None)
        _copy.build(board_copy, self.moves, self.player, self.boxes, self.goals, self.points)

        return _copy

    # Comparamos por el costo
    def __lt__(self, other):
        return len(self.moves) < len(other.moves)

    def print_board(self):
        for row in self.board:
            for elem in row:
                print(elem.value, end="")
            print("")
