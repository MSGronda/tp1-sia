import math

# Hace un promedio (creo) que de forma eficiente del manhattan y euclidian
def calculate_average_distance(board):

    boxes = board.get_boxes()

    goal_locations = board.get_goals()


    sum_distance_euclid = 0
    sum_distance_manhattan = 0
    minimum_distance_euclid = None
    minimum_distance_manhattan = None

    for box_position in boxes:
        for goal_location in goal_locations:

            distance_euclid = math.dist(box_position, goal_location)
            distance_manhattan = abs(box_position[0] - goal_location[0]) + abs(box_position[1] - goal_location[1])

            if minimum_distance_euclid is None or distance_euclid < minimum_distance_euclid:
                minimum_distance_euclid = distance_euclid

            if minimum_distance_manhattan is None or distance_manhattan < minimum_distance_manhattan:
                minimum_distance_manhattan = distance_manhattan

        sum_distance_euclid += minimum_distance_euclid
        sum_distance_manhattan += minimum_distance_manhattan

    return max(sum_distance_manhattan, sum_distance_euclid)