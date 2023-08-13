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
        self.player_y = None
        self.player_x = None
        self.moves = []

        if path is not None:
            # Matriz de n x m
            board = generate_board(path)
            self.build(board, [])

    # Sirve para cuando hagamos deepcopy
    def build(self, board, moves):

        self.board = board
        self.moves = copy.deepcopy(moves)

        self.height, self.width = np.shape(self.board)

        self.count_goals()
        # Nos guardamos la pos del jugador para no tener que ir buscandolo

        y, x = self.find_player()

        if x == -1 or y == -1:
            quit("no player found")

        self.player_x = x
        self.player_y = y

    # METODOS "PRIVADOS"

    def find_player(self):
        condition = np.logical_or(self.board == BoardItems.PLAYER, self.board == BoardItems.GOAL_WITH_PLAYER)

        row_indexes, col_indexes = np.where(condition)

        if len(row_indexes) == 0 or len(col_indexes) == 0:
            return -1, -1

        return row_indexes[0], col_indexes[0]

    def count_goals(self):
        self.goals = 0
        self.points = 0

        for row in self.board:
            for item in row:
                if item == BoardItems.GOAL or item == BoardItems.GOAL_WITH_PLAYER:
                    self.goals += 1
                elif item == BoardItems.GOAL_WITH_BOX:
                    self.goals += 1
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
        if 0 <= self.player_x + move.value[MOVE_X] < self.width and 0 <= self.player_y + move.value[
            MOVE_Y] < self.height:

            block = self.board[self.player_y + move.value[MOVE_Y], self.player_x + move.value[MOVE_X]]

            # Caso: me muevo a un espacio vacio
            if block == BoardItems.EMPTY_SPACE or block == BoardItems.GOAL:
                return True

            # Caso: quiere mover una caja
            elif block == BoardItems.BOX or block == BoardItems.GOAL_WITH_BOX:

                # Me fijo que adonde quiero empujar la caja, es dentro de la matriz
                if 0 <= self.player_x + move.value[MOVE_X] * 2 < self.width and 0 <= self.player_y + move.value[
                    MOVE_Y] * 2 < self.height:

                    move_to_block = self.board[
                        self.player_y + move.value[MOVE_Y] * 2, self.player_x + move.value[MOVE_X] * 2]

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
        old_pos_block = self.board[self.player_y, self.player_x]

        if old_pos_block == BoardItems.PLAYER:
            self.board[self.player_y, self.player_x] = BoardItems.EMPTY_SPACE
        elif old_pos_block == BoardItems.GOAL_WITH_PLAYER:
            self.board[self.player_y, self.player_x] = BoardItems.GOAL

        # Cambio la nueva posicion del jugador
        self.player_x += move.value[MOVE_X]
        self.player_y += move.value[MOVE_Y]

        new_pos_block = self.board[self.player_y, self.player_x]

        if new_pos_block == BoardItems.EMPTY_SPACE:
            self.board[self.player_y, self.player_x] = BoardItems.PLAYER
        elif new_pos_block == BoardItems.GOAL:
            self.board[self.player_y, self.player_x] = BoardItems.GOAL_WITH_PLAYER
        # Caso: quiero mover un caja
        elif new_pos_block == BoardItems.BOX or new_pos_block == BoardItems.GOAL_WITH_BOX:

            # Ahora el jugador esta donde estaba la caja
            if new_pos_block == BoardItems.BOX:
                self.board[self.player_y, self.player_x] = BoardItems.PLAYER
            else:
                # Desplace la caja de un goal
                self.board[self.player_y, self.player_x] = BoardItems.GOAL_WITH_PLAYER

                # La caja deja de estar encima de un goal => pierdo un punto
                self.points -= 1

            # Muevo la caja a la nueva posicion
            new_pos_box_block = self.board[self.player_y + move.value[MOVE_Y], self.player_x + move.value[MOVE_X]]

            if new_pos_box_block == BoardItems.EMPTY_SPACE:
                self.board[self.player_y + move.value[MOVE_Y], self.player_x + move.value[MOVE_X]] = BoardItems.BOX
            elif new_pos_box_block == BoardItems.GOAL:
                self.board[
                    self.player_y + move.value[MOVE_Y], self.player_x + move.value[MOVE_X]] = BoardItems.GOAL_WITH_BOX

                # La caja esta encima de un goal => consigo un punto
                self.points += 1

    def get_points(self):
        return self.points

    def get_goals(self):
        return self.goals

    def get_board(self):
        return self.board

    def victory(self):
        return self.points == self.goals

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
        _copy.build(board_copy, self.moves)

        return _copy

    def __lt__(self, other):
        return self.points < other.points

    def find_board_component(self, components: [BoardItems]):
        coordinates = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] in components:
                    coordinates.append((i, j))
        return coordinates



    def calculate_manhattan_distance(self):
        # devuelve array de tuplas representando posicion cajas [(1,2), (3,4), ...]
        boxes = self.find_board_component([BoardItems.BOX])
        # idem pero para posiciones goal
        goal_locations = self.find_board_component([BoardItems.GOAL,BoardItems.GOAL_WITH_PLAYER])

        # calcula la distancia de las sumas minimas de las cajas a su goal position.
        sum_distance = 0
        minimum_distance = None

        for box_position in boxes:
            for goal_location in goal_locations:
                # calculo distancia entre cajas
                distance = abs(box_position[0] - goal_location[0]) + abs(box_position[1] - goal_location[1])
                if minimum_distance is None or distance < minimum_distance:
                    minimum_distance = distance

            sum_distance += minimum_distance



        return sum_distance

    def print_board(self):
        for row in self.board:
            for elem in row:
                print(elem.value, end="")
            print("")
