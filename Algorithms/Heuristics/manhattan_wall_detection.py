from src.sokoban import BoardItems


def calculate_manhattan_distance_wall_detection(game):
    # devuelve array de tuplas representando posicion cajas [(1,2), (3,4), ...]
    boxes = game.get_boxes()
    # idem pero para posiciones goal
    goal_locations = game.get_goals()

    # calcula la distancia de las sumas minimas de las cajas a su goal position.
    sum_distance = 0
    minimum_distance = None

    for box_position in boxes:
        for goal_location in goal_locations:
            # calculo distancia entre cajas
            distance = abs(box_position[0] - goal_location[0]) + abs(box_position[1] - goal_location[1])

            if box_position[0] > goal_location[0]:
                x1 = goal_location[0]
                x2 = box_position[0]
            else:
                x1 = box_position[0]
                x2 = goal_location[0]

            if box_position[1] > goal_location[1]:
                y1 = goal_location[1]
                y2 = box_position[1]
            else:
                y1 = box_position[1]
                y2 = goal_location[1]

            board = game.get_board()

            blocking_factor = 0

            for i in range(x1, x2):
                if board[y1, i] == BoardItems.WALL:
                    blocking_factor += 0.5
                if board[y2, i] == BoardItems.WALL:
                    blocking_factor += 0.5

            for j in range(y1, y2):
                if board[j, x2] == BoardItems.WALL:
                    blocking_factor += 0.5
                if board[j, x1] == BoardItems.WALL:
                    blocking_factor += 0.5

            distance += blocking_factor

            if minimum_distance is None or distance < minimum_distance:
                minimum_distance = distance

        sum_distance += minimum_distance

    return sum_distance
