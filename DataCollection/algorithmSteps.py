import csv
import pandas as pd
import plotly.express as px
from DataCollection import check
from Algorithms.bfs import bfs
from Algorithms.dfs import dfs
from Algorithms.greedy import greedy
from Algorithms.a_star import a_star

def algorithmSteps(board,heuristic):
    check.check_results_directory()
    with open(f"../Results/algorithm-steps.csv", "w") as f:
        #BFS
        print("Running BFS")
        _, _, solution_exists, bfs_game, _, _ = bfs(board)
        # print(solution_exists)
        print(f"BFS, {len(bfs_game.moves)}", file=f)

        #DFS
        print("Running DFS")
        _, _, dfs_solution_exists, dfs_game, _, _ = dfs(board)
        print(f"DFS, {len(dfs_game.moves)}", file=f)


        #GREEDY
        _, _, solution_exists, result , _ , _ = greedy(board, heuristic)
        print("Running Greedy")
        print(f"GREEDY, {len(result.moves)}", file=f)

        #A*
        print("Running A*")
        _, _, solution_exists, a_star_game, _, _ = a_star(board, heuristic)
        print(f"A*, {len(a_star_game.moves)}", file=f)

    data = []
    with open(f"../Results/algorithm-steps.csv", "r") as stepdata:
        reader = csv.reader(stepdata)
        for algorithm, steps in reader:
            data.append({
                "Algorithm": algorithm,
                "Steps": int(steps)
            })

    df = pd.DataFrame(data)

    fig = px.bar(df, x='Algorithm', y='Steps', title='Solution Steps for Algorithm', color="Algorithm",
                    text='Steps',  # Add this to include the step values as text labels
                    labels={'Steps': 'Steps'}  # You can customize the label here
                 )
    fig.update_traces(texttemplate='%{text}', textposition='auto')  # Set the text label format and position
    fig.update_yaxes(range=[0, max(df['Steps']) + 2])  # Adjust the range_y to include some margin above the max value
    fig.show()




