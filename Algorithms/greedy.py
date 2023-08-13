import time


from src.sokoban import *
from src.BoardTree import BoardTreeNode

game = Sokoban("../Boards/board.txt")
print("running")

mainNode = BoardTreeNode(game)

print(mainNode.expand())
