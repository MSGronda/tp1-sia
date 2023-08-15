import time

from src.sokoban import *
from src.BoardTree import BoardTreeNode


def greedy(board, heuristicStrategy):
    game = Sokoban(board)
    print("running")

    BoardTreeNode.heuristicStrategy = heuristicStrategy #seteo la heuristica
    mainNode = BoardTreeNode(game)

    start = time.time()
    #result = mainNode.expand() #version reecursiva
    result = mainNode.iterative_expand() #version iterativa
    end = time.time()
    #print(f"{result.moves}\ntook {end - start}s")
    return end, start, result


