import math
import aux
from Algorithms import bfs
from Algorithms import dfs
from Algorithms import greedy
from Algorithms import a_star
import csv
import plotly.graph_objects as go
import plotly.colors as pc
import numpy as np


from Algorithms.Heuristics.manhattan_distance import calculate_manhattan_distance
from Algorithms.Heuristics.euclidian_distance import calculate_euclidian_distance
from Algorithms.Heuristics.average_distance import calculate_average_distance



aux.check_results_directory()

board = "../Boards/board.txt"
ITERATIONS = 100



with open(f"../Results/algorithm-times.csv", "w") as f:

    for _ in range(ITERATIONS):
        #BFS
        bfs_end_time, bfs_start_time, solution_exists, _, _, _ = bfs.bfs(board)

        bfs_time = bfs_end_time - bfs_start_time
        print(f"BFS, {bfs_time}", file=f)

    for _ in range(ITERATIONS):
        #DFS
        dfs_end_time, dfs_start_time, solution_exists, _, _, _ = dfs.dfs(board)

        dfs_time = dfs_end_time - dfs_start_time
        print(f"DFS, {dfs_time}", file=f)

    for _ in range(ITERATIONS):
        #GREEDY
        greedy_end_time, greedy_start_time, result = greedy.greedy(board,calculate_euclidian_distance)

        greedy_time = greedy_end_time - greedy_start_time
        print(f"GREEDY, {greedy_time}", file=f)
    for _ in range(ITERATIONS):
        #A*
        Astar_end_time, Astar_start_time, solution_exists, _, _, _ = a_star.a_star(board,calculate_manhattan_distance)

        Astar_time = Astar_end_time - Astar_start_time
        print(f"A_STAR, {Astar_time}", file=f)


bfs_data = []
dfs_data = []
greedy_data = []
Astar_data = []
with open(f"../Results/algorithm-times.csv", "r") as timedata:
    reader = csv.reader(timedata)
    for algorithm, time in reader:
        if algorithm == 'BFS':
            bfs_data.append(float(time))
        elif algorithm == 'DFS':
            dfs_data.append(float(time))
        elif algorithm =='A_STAR':
            Astar_data.append(float(time))
        else:
            greedy_data.append(float(time))

bfs_data = np.array(bfs_data)
dfs_data = np.array(dfs_data)
greedy_data = np.array(greedy_data)
Astar_data = np.array(Astar_data)

bfs_mean = np.mean(bfs_data)
dfs_mean = np.mean(dfs_data)
greedy_mean = np.mean(greedy_data)
Astar_mean = np.mean(Astar_data)

bfs_error = np.std(bfs_data) / math.sqrt(ITERATIONS)
dfs_error = np.std(dfs_data) / math.sqrt(ITERATIONS)
greedy_error = np.std(greedy_data) / math.sqrt(ITERATIONS)
Astar_error = np.std(Astar_data) / math.sqrt(ITERATIONS)

algorithms = ['BFS', 'DFS', 'GREEDY', 'A*']
x_pos = np.arange(len(algorithms))
CTEs = [bfs_mean, dfs_mean, greedy_mean, Astar_mean]
error = [bfs_error, dfs_error, greedy_error, Astar_error]

num_colors = len(algorithms)
distinct_colors = pc.qualitative.Plotly * int(np.ceil(num_colors / len(pc.qualitative.Plotly)))

# Create a bar chart with error bars
data = [
    go.Bar(
        x=algorithms,
        y=CTEs,
        error_y=dict(type='data', array=error, visible=True),
        marker_color=distinct_colors,
        opacity=0.6
    )
]

layout = go.Layout(
    title='Algorithm Performance Comparison',
    xaxis=dict(title='Algorithms'),
    yaxis=dict(title='Time'),
    showlegend=False
)

fig = go.Figure(data=data, layout=layout)
fig.show()

