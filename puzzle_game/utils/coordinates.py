from enum import Enum


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x_distance(self, x_coord):
        return abs(self.x - x_coord)

    def get_y_distance(self, y_coord):
        return abs(self.y - y_coord)

    def move(self, direction):
        if direction == Directions.RIGHT:
            self.x += 1
        elif direction == Directions.LEFT:
            self.x -= 1
        elif direction == Directions.UP:
            self.y -= 1
        elif direction == Directions.DOWN:
            self.y += 1


class Directions(Enum):
    UP = 1,
    DOWN = 2,
    LEFT = 3,
    RIGHT = 4
