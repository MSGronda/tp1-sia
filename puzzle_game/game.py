from puzzle_game.utils.coordinates import Coordinates, Directions
import copy

BOARDSIZE = 3


def get_empty_matrix(size):
    return [[0] * size for _ in range(size)]


class Game:
    solvedBoardMatrix = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]

    solvedBoardMap = {0: Coordinates(1, 1), 1: Coordinates(0, 0), 2: Coordinates(1, 0),
                      3: Coordinates(2, 0), 4: Coordinates(2, 1), 5: Coordinates(2, 2),
                      6: Coordinates(1, 2), 7: Coordinates(0, 2), 8: Coordinates(0, 1)}

    def __init__(self, pathToBoard):
        if pathToBoard is not None:
            self.board = self.load_board(pathToBoard)

    def __hash__(self):
        hash = 0
        for y_axis in range(BOARDSIZE):
            for x_axis in range(BOARDSIZE):
                hash *= 10
                hash += self.board[y_axis][x_axis]
        return hash

    def load_board(self, pathToBoard):
        with open(pathToBoard) as boardInfoFile:
            numbers = boardInfoFile.read(BOARDSIZE ** 2)
            boardToReturn = get_empty_matrix(BOARDSIZE)  # Initialize the board with 0s
            iterator = 0
            for x_axis in range(BOARDSIZE):
                for y_axis in range(BOARDSIZE):
                    boardToReturn[x_axis][y_axis] = int(numbers[iterator])
                    iterator += 1
            return boardToReturn

    def is_solved(self):
        return self.board == self.solvedBoardMatrix

    def can_move(self, direction):
        blank_space_coordinates = self.get_blank_space_coordinates()
        blank_space_coordinates.move(direction)
        return 0 <= blank_space_coordinates.x < BOARDSIZE and 0 <= blank_space_coordinates.y < BOARDSIZE

    def get_blank_space_coordinates(self):
        blank_space_coordinates = None
        for x_axis in range(BOARDSIZE):
            for y_axis in range(BOARDSIZE):
                if self.board[y_axis][x_axis] == 0:
                    blank_space_coordinates = Coordinates(x_axis, y_axis)
        return blank_space_coordinates

    def get_possible_moves(self):
        blank_space_coordinates = self.get_blank_space_coordinates()
        possible_moves = []
        for move in Directions:
            if self.can_move(move, blank_space_coordinates):
                possible_moves.append(move)
        return possible_moves

    def swap(self, x1, y1, x2, y2):
        self.board[y1][x1], self.board[y2][x2] = self.board[y2][x2], self.board[y1][x1]

    def move(self, direction):
        blank_space_coordinates = self.get_blank_space_coordinates()
        x = blank_space_coordinates.x
        y = blank_space_coordinates.y

        if direction == Directions.RIGHT:
            self.swap(x, y, x+1, y)
        elif direction == Directions.LEFT:
            self.swap(x, y, x-1, y)
        elif direction == Directions.UP:
            self.swap(x, y, x, y-1)
        elif direction == Directions.DOWN:
            self.swap(x, y, x, y+1)

    def get_new_game_by_move(self, direction):
        new_game = copy.deepcopy(self)
        new_game.move(direction)
        return new_game
