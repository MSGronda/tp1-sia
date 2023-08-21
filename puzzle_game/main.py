from puzzle_game.gameSolver import gameSolver
import json

with open("./config.json", "r") as configFile:
    configurationData = json.load(configFile)

for config in configurationData:
    print(f"Solving board {config['boardToSolve']} with algorithm \"{config['algorithmToUse']}\" and heuristic \"{config['heuristicToUse']}\"")
    gameSolver(config["boardToSolve"], config["algorithmToUse"], config["heuristicToUse"])
    print()
