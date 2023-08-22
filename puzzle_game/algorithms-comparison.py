from puzzle_game.gameSolver import gameSolver
from puzzle_game.graphs.algorithmsGraph import createAlgorithmsGraph
import json

data_to_plot = {}  # Dictionary to store solution depths for each heuristic

with open("configs/algorithm-comparison-config.json", "r") as configFile:
    configurationData = json.load(configFile)

for config in configurationData:
    boardToSolve = config['boardToSolve']
    algorithmToUse = config['algorithmToUse']
    heuristicTouse = config['heuristicToUse']

    print(f"Solving board {boardToSolve} with algorithm \"{algorithmToUse}\" and heuristic \"{heuristicTouse}\"")
    expandedNodes, solution_depth = gameSolver(config["boardToSolve"], config["algorithmToUse"], config["heuristicToUse"])
    print(f"Game is solved! All it took was to expand {expandedNodes} nodes")
    print(f"The depth of the answer is {solution_depth}")
    print()

    # Store solution depth in the data_to_plot dictionary
    if boardToSolve not in data_to_plot:
        data_to_plot[boardToSolve] = {}
    data_to_plot[boardToSolve][algorithmToUse] = expandedNodes

createAlgorithmsGraph(data_to_plot)



