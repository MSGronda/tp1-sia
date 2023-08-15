def calculate_manhattan_distance(board):
    # devuelve array de tuplas representando posicion cajas [(1,2), (3,4), ...]
    boxes = board.get_boxes()
    # idem pero para posiciones goal
    goal_locations = board.get_goals()

    # calcula la distancia de las sumas minimas de las cajas a su goal position.
    sum_distance = 0
    minimum_distance = None

    for box_position in boxes:
        for goal_location in goal_locations:
            # calculo distancia entre cajas
            distance = abs(box_position[0] - goal_location[0]) + abs(box_position[1] - goal_location[1])
            if minimum_distance is None or distance < minimum_distance:
                minimum_distance = distance

        sum_distance += minimum_distance

    return sum_distance