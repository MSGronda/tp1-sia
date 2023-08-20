import csv
import pandas as pd
import plotly.express as px
from Algorithms.Heuristics.combined_heuristic import combined_heuristic
from DataCollection import check
from Algorithms.bfs import bfs
from Algorithms.dfs import dfs
from Algorithms.greedy import greedy
from Algorithms.a_star import a_star

def algorithmFrontier(board, heuristic):
    check.check_results_directory()
    with open(f"../Results/algorithm-frontier.csv", "w") as f:
        #BFS
        print("Running BFS")
        _, _, solution_exists, _, _, nodes_left_bfs = bfs(board)
        # print(solution_exists)
        print(f"BFS, {nodes_left_bfs}", file=f)

        #DFS
        print("Running DFS")
        _, _, dfs_solution_exists, _, _, nodes_left_dfs = dfs(board)
        print(f"DFS, {nodes_left_dfs}", file=f)


        #GREEDY
        _, _, solution_exists, _, _, nodes_left_greedy = greedy(board, heuristic)
        print("Running Greedy")
        print(f"GREEDY, {nodes_left_greedy}", file=f)

        #A*
        print("Running A*")
        _, _, solution_exists, _, _, nodes_left_astar = a_star(board, heuristic)
        print(f"A*, {nodes_left_astar}", file=f)

    data = []
    with open(f"../Results/algorithm-frontier.csv", "r") as node_data:
        reader = csv.reader(node_data)
        for algorithm, nodes in reader:
            data.append({
                "Algorithm": algorithm,
                "# Nodes in frontier": int(nodes)
            })

    df = pd.DataFrame(data)

    fig = px.bar(df, x='Algorithm', y='# Nodes in frontier', title='Number of nodes in frontier', color="Algorithm",
                    text='# Nodes in frontier',
                    labels={'# Nodes in frontier': '# Nodes in frontier'}
                 )
    fig.update_traces(texttemplate='%{text}', textposition='auto')
    fig.update_yaxes(range=[0, max(df['# Nodes in frontier']) + 2])
    fig.show()




