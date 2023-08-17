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
    DEAD_ZONE = 'x'


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
    'x': BoardItems.DEAD_ZONE
}

WALL_MAP = {
    Moves.UP: 0,
    Moves.LEFT: 1,
    Moves.RIGHT: 2,
    Moves.DOWN: 3
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

        self.moves = None

        self.player = None
        self.boxes = None
        self.goals = None

        self.points = 0

        if path is not None:
            # Matriz de n x m
            board = generate_board(path)
            self.build(board, [])

    # Sirve para cuando hagamos deepcopy
    def build(self, board, moves, player=None, boxes=None, goals=None, points=0):
        self.board = board
        self.moves = copy.deepcopy(moves)

        self.height, self.width = np.shape(self.board)

        # Por eficiencia, puedo direcatmente pasarle una copia de los locations
        # o lo puede calcular por su cuenta.
        if player is None or boxes is None or goals is None:
            self.boxes = []
            self.goals = []
            self.locate_items()
        else:
            self.player = copy.deepcopy(player)
            self.boxes = copy.deepcopy(boxes)
            self.goals = goals
            self.points = points

    # METODOS "PRIVADOS"

    def locate_items(self):

        # Consigo la posicion de todos los elementos relevantes
        # para no tener que iterar constantemente

        for y, row in enumerate(self.board):
            for x, item in enumerate(row):

                if item == BoardItems.PLAYER:
                    self.player = [x, y]

                    self.board[y, x] = BoardItems.EMPTY_SPACE  # Convierto a estatico
                elif item == BoardItems.GOAL_WITH_PLAYER:
                    self.player = [x, y]
                    self.goals.append((x, y))

                    self.board[y, x] = BoardItems.GOAL  # Convierto a estatico
                elif item == BoardItems.BOX:
                    self.boxes.append((x, y))

                    self.board[y, x] = BoardItems.EMPTY_SPACE  # Convierto a estatico
                elif item == BoardItems.GOAL:
                    self.goals.append((x, y))
                elif item == BoardItems.GOAL_WITH_BOX:
                    self.boxes.append((x, y))
                    self.goals.append((x, y))

                    self.points += 1

                    self.board[y, x] = BoardItems.GOAL  # Convierto a estatico

                # Calculamos los dead zones
                if self.board[y, x] == BoardItems.EMPTY_SPACE:
                    walls = [0, 0, 0, 0]
                    for move in Moves:
                        adj_x = x + move.value[COORD_X]
                        adj_y = y + move.value[COORD_Y]

                        if 0 <= adj_x < self.width and 0 <= adj_y < self.height:
                            if self.board[adj_y, adj_x] == BoardItems.WALL:
                                walls[WALL_MAP[move]] = 1

                    if (walls[WALL_MAP[Moves.UP]] == walls[WALL_MAP[Moves.LEFT]] == 1 or
                            walls[WALL_MAP[Moves.UP]] == walls[WALL_MAP[Moves.RIGHT]] == 1 or
                            walls[WALL_MAP[Moves.DOWN]] == walls[WALL_MAP[Moves.LEFT]] == 1 or
                            walls[WALL_MAP[Moves.DOWN]] == walls[WALL_MAP[Moves.RIGHT]] == 1):
                        self.board[y, x] = BoardItems.DEAD_ZONE

    # METODOS "PUBLICOS"

    def get_valid_moves(self):
        valid_moves = []
        for move in Moves:
            if self.can_move(move):
                valid_moves.append(move)
        return valid_moves

    def can_move(self, move):
        new_x = self.player[COORD_X] + move.value[MOVE_X]
        new_y = self.player[COORD_Y] + move.value[MOVE_Y]

        if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height:
            return False

        # Caso: me choco contra la pared
        if self.board[new_y, new_x] == BoardItems.WALL:
            return False

        # Caso: quiero mover una caja
        if (new_x, new_y) in self.boxes:
            new_box_x = new_x + move.value[MOVE_X]
            new_box_y = new_y + move.value[MOVE_Y]

            # Caso: quiero mover la caja por fuera del mapa
            if new_box_x < 0 or new_box_x >= self.width or new_box_y < 0 or new_box_y >= self.height:
                return False

            # Caso: donde quiero mover la caja hay una pared
            if self.board[new_box_y, new_box_x] == BoardItems.WALL:
                return False

            # Caso: donde quiero mover la caja hay otra caja
            if (new_box_x, new_box_y) in self.boxes:
                return False

        return True

    def move(self, move):
        if not self.can_move(move):
            return

        # Agrego el movimiento a los moviemientos hechos
        self.moves.append(move)

        # La nueva posicion del jugador
        new_x = self.player[COORD_X] + move.value[MOVE_X]
        new_y = self.player[COORD_Y] + move.value[MOVE_Y]

        # Caso: quiero mover una caja
        if (new_x, new_y) in self.boxes:

            # Caso: lo saque de un goal
            if self.board[new_y, new_x] == BoardItems.GOAL:
                self.points -= 1

            new_box_x = new_x + move.value[MOVE_X]
            new_box_y = new_y + move.value[MOVE_Y]

            # Updateo la posicion en la lista de posiciones de cajas
            idx = self.boxes.index((new_x, new_y))
            self.boxes[idx] = (new_box_x, new_box_y)

            # Caso: lo puse encima de un goal
            if self.board[new_box_y, new_box_x] == BoardItems.GOAL:
                self.points += 1

        self.player[COORD_X] = new_x
        self.player[COORD_Y] = new_y

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
        self.boxes.sort()
        return hash(str(self.player) + str(self.boxes))

    def __eq__(self, other):
        self.boxes.sort()
        other.boxes.sort()
        return self.player == other.player and self.boxes == other.boxes

    def __deepcopy__(self, memo=None):
        _copy = Sokoban(None)
        _copy.build(self.board, self.moves, self.player, self.boxes, self.goals, self.points)

        return _copy

    # Comparamos por el costo
    def __lt__(self, other):
        return len(self.moves) < len(other.moves)

    def print_board(self):
        for row in self.board:
            for elem in row:
                print(elem.value, end="")
            print("")
