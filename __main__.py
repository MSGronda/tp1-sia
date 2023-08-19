import copy
import json

from src.sokoban import Sokoban
from Algorithms.bfs import bfs
from Algorithms.dfs import dfs
from Algorithms.greedy import greedy
from Algorithms.a_star import a_star
from Algorithms.Heuristics.manhattan_distance import calculate_manhattan_distance
from Algorithms.Heuristics.combined_heuristic import combined_heuristic
from Algorithms.Heuristics.euclidian_distance import calculate_euclidian_distance
from Algorithms.Heuristics.lost_game import lost_game_heuristic
from Algorithms.Heuristics.manhattan_wall_detection import calculate_manhattan_distance_wall_detection
from Algorithms.Heuristics.average_distance import calculate_average_distance

FUNCMAP = {"bfs": bfs, "dfs": dfs, "greedy": greedy, "a_star": a_star}
HEURISTICSMAP = {"average_distance": calculate_average_distance,
                 "manhattan_wall_detection": calculate_manhattan_distance_wall_detection,
                 "manhattan_distance": calculate_manhattan_distance, "combined_heuristic": combined_heuristic,
                 "euclidian_distance": calculate_euclidian_distance, "lost_game": lost_game_heuristic}


# Resultado(éxito / fracaso)(si es aplicable)
# Costo de la solución OK
# Cantidad de nodos expandidos OK
# Cantidad de nodos frontera OK
# Solución(camino desde estado inicial al final) OK
# Tiempo de procesamiento OK
def runSingleAlgorithm(data: dict):
    if not data["run"]:
        return
    boardPath = data["board"]
    function = FUNCMAP[data["algorithm"]]
    heuristic_name = data["heuristic"]
    end, start, solution_exists, game, nodesExpanded, frontierNodesLeft = function(boardPath, HEURISTICSMAP[
        heuristic_name] if heuristic_name in HEURISTICSMAP.keys() else None)
    if solution_exists:
        if data["showBoardMoves"]:
            current_game = Sokoban(boardPath)
            print("--------------------------STEP 0---------------------------")
            print(current_game)
            for idx, movement in enumerate(game.moves):
                current_game.move(movement)
                print(f"--------------------------STEP {idx + 1}---------------------------")
                print(current_game)
                print(f"player used: {movement}")
        print(f"Solution found, cost:{len(game.moves)} steps")
        print(game.moves)
        print(f"Solution found in {end - start} seconds")
        print(f"expanded {nodesExpanded} nodes")
        print(f"{frontierNodesLeft} nodes left on frontier")
    else:
        print("No solution was found")


with open("configuration.json", "r") as f:
    configFile = json.load(f)

runSingleAlgorithm(configFile["singleAlgorithmData"])
