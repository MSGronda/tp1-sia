from puzzle_game.game import *


# Sum of Manhattan distance for each box to its final position
def get_total_manhattan(board):
    total_manhattan = 0
    for x_axis in range(BOARDSIZE):
        for y_axis in range(BOARDSIZE):
            current_number = board[y_axis][x_axis]
            if current_number != 0:
                desired_coordinates = Game.solvedBoardMap[current_number]
                total_manhattan += desired_coordinates.get_x_distance(x_axis)
                total_manhattan += desired_coordinates.get_y_distance(y_axis)
    return total_manhattan
