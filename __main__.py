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
from DataCollection.heuristicsComparison import heuristicsComparison
from DataCollection.algorithmTimes import algorithmTimes
from DataCollection.algorithmSteps import algorithmSteps
from DataCollection.algorithmFrontier import algorithmFrontier
from DataCollection.algorithmNodes import algorithmNodes

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

def runAlgorithmNodes(data: dict):
    if not data["run"]:
        return
    heuristic_name = data["heuristic"]
    algorithmNodes(f"./boards/{data['board']}", HEURISTICSMAP[heuristic_name])


def runAlgorithmFrontier(data: dict):
    if not data["run"]:
        return
    heuristic_name = data["heuristic"]
    algorithmFrontier(f"./boards/{data['board']}", HEURISTICSMAP[heuristic_name])


def runAlgorithmSteps(data: dict):
    if not data["run"]:
        return
    heuristic_name = data["heuristic"]
    algorithmSteps(f"./Boards/{data['board']}", HEURISTICSMAP[heuristic_name])


def runAlgorithmTimes(data: dict):
    if not data["run"]:
        return
    heuristic_name = data["heuristic"]
    algorithmTimes(data["iterations"], f"./Boards/{data['board']}", HEURISTICSMAP[heuristic_name])


def runHeuristicsComparison(data: dict):
    if not data["run"]:
        return
    heuristicsComparison(data["iterations"], f"./Boards/{data['board']}")


def runSingleAlgorithm(data: dict):
    if not data["run"]:
        return
    boardPath = f"./Boards/{data['board']}"
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
runHeuristicsComparison(configFile["heuristicsComparison"])
runAlgorithmTimes(configFile["timesComparison"])
runAlgorithmSteps(configFile["stepsComparison"])
runAlgorithmFrontier(configFile["frontierComparison"])
runAlgorithmNodes(configFile["nodesExpandedComparison"])
