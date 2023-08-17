from src.sokoban import *

INFINITY = 10000000000000

def lost_game_heuristic(game):
    board = game.get_board()
    for box in game.get_boxes():
        if board[box[COORD_Y], box[COORD_X]] == BoardItems.DEAD_ZONE:
            return INFINITY

    return 0
