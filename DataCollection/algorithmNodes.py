import csv
import pandas as pd
import plotly.express as px
from Algorithms.Heuristics.combined_heuristic import combined_heuristic
from DataCollection import check
from Algorithms.bfs import bfs
from Algorithms.dfs import dfs
from Algorithms.greedy import greedy
from Algorithms.a_star import a_star

def algorithmNodes(board, heuristic):
    check.check_results_directory()
    with open(f"../Results/algorithm-nodes.csv", "w") as f:
        #BFS
        print("Running BFS")
        _, _, solution_exists, _, nodes_bfs, _ = bfs(board)
        # print(solution_exists)
        print(f"BFS, {nodes_bfs}", file=f)

        #DFS
        print("Running DFS")
        _, _, dfs_solution_exists, _, nodes_dfs, _ = dfs(board)
        print(f"DFS, {nodes_dfs}", file=f)


        #GREEDY
        _, _, solution_exists, _, nodes_greedy, _ = greedy(board, heuristic)
        print("Running Greedy")
        print(f"GREEDY, {nodes_greedy}", file=f)

        #A*
        print("Running A*")
        _, _, solution_exists, _, nodes_star, _ = a_star(board, heuristic)
        print(f"A*, {nodes_star}", file=f)

    data = []
    with open(f"../Results/algorithm-nodes.csv", "r") as node_data:
        reader = csv.reader(node_data)
        for algorithm, nodes in reader:
            data.append({
                "Algorithm": algorithm,
                "# Nodes expanded": int(nodes)
            })

    df = pd.DataFrame(data)

    fig = px.bar(df, x='Algorithm', y='# Nodes expanded', title='Number of nodes expanded during solve', color="Algorithm",
                    text='# Nodes expanded',
                    labels={'# Nodes expanded': '# Nodes expanded'}
                 )
    fig.update_traces(texttemplate='%{text}', textposition='auto')
    fig.update_yaxes(range=[0, max(df['# Nodes expanded']) + 2])
    fig.show()


algorithmNodes("../Boards/board2.txt", combined_heuristic)


