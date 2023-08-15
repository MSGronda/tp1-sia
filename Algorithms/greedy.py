import time

from src.sokoban import *
from src.BoardTree import BoardTreeNode


def greedy():
    game = Sokoban("../Boards/board.txt")
    print("running")

    mainNode = BoardTreeNode(game)

    start = time.time()
    result = mainNode.expand() #version reecursiva
    #result = mainNode.iterative_expand() #version iterativa
    end = time.time()
    #print(f"{result.moves}\ntook {end - start}s")
    return end, start, result


# print(f"time it took: {end - start}")
# print(result.moves if result else "No solution was found")
