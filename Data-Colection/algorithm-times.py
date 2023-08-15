import subprocess
from Algorithms.bfs import bfs
from Algorithms.dfs import dfs
from Algorithms.greedy import greedy
import csv
import pandas as pd
import plotly.express as px


board = "../Boards/board2.txt"
ITERATIONS = 100
bfs_time = 0
dfs_time = 0
greedy_time = 0
for _ in range(ITERATIONS):
    #BFS
    bfs_end_time, bfs_start_time, _, _, _, _ = bfs(board)

    bfs_time += bfs_end_time - bfs_start_time

    #DFS
    dfs_end_time, dfs_start_time, _, _, _, _ = dfs(board)

    dfs_time += dfs_end_time - dfs_start_time

    #GREEDY
    greedy_end_time, greedy_start_time, result = greedy(board)

    greedy_time += greedy_end_time - greedy_start_time

bfs_time /= ITERATIONS
dfs_time /= ITERATIONS
greedy_time /= ITERATIONS

with open(f"../Results/algorithm-times.csv", "w") as f:
    print(f"BFS, {round(bfs_time,5)}", file=f)
    print(f"DFS, {round(dfs_time,5)}", file=f)
    print(f"GREEDY, {round(greedy_time,5)}", file=f)

data = []
with open(f"../Results/algorithm-times.csv", "r") as timedata:
    reader = csv.reader(timedata)

    for algorithm, time in reader:
        data.append({'Algorithm': algorithm, 'Time': float(time)})

df = pd.DataFrame(data)

df['Time'] = df['Time'].apply(lambda x: round(x, 5))  # Round 'Time' values

fig = px.bar(df, x="Algorithm", y="Time", color="Algorithm", title="Time taken for algorithms in trivial map")
fig.show()