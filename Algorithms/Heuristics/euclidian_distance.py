import math


def calculate_euclidian_distance(board):

    boxes = board.get_boxes()

    goal_locations = board.get_goals()


    sum_distance = 0
    minimum_distance = None

    for box_position in boxes:
        for goal_location in goal_locations:

            distance = math.dist(box_position, goal_location)

            if minimum_distance is None or distance < minimum_distance:
                minimum_distance = distance

        sum_distance += minimum_distance

    return sum_distance