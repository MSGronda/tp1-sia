import time


from src.sokoban import *
from src.BoardTree import BoardTreeNode

game = Sokoban("../Boards/board4.txt")
print("running")

mainNode = BoardTreeNode(game)

start = time.time()
result = mainNode.expand()
end = time.time()
print(f"time it took: {end - start}")
print(result.moves if result else "No solution was found")

