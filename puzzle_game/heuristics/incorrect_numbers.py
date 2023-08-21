from puzzle_game.game import *


# Sum of numbers in incorrect position
def get_sum_incorrect(board):
    sum = 0
    for x_axis in range(BOARDSIZE):
        for y_axis in range(BOARDSIZE):
            if Game.solvedBoardMatrix[y_axis][x_axis] != board[y_axis][x_axis]:
                sum += 1
    return sum
