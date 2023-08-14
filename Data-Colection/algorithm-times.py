import subprocess
from Algorithms.bfs import bfs
from Algorithms.dfs import dfs
from Algorithms.greedy import greedy


# result = subprocess.run(["python", "../Algorithms/bfs.py"], stdout=subprocess.PIPE, text=True)

#BFS
bfs_end_time, bfs_start_time, _, _, _, _ = bfs()

bfs_time = bfs_end_time - bfs_start_time

#DFS
dfs_end_time, dfs_start_time, _, _, _, _ = dfs()

dfs_time = dfs_end_time - dfs_start_time

#GREEDY
greedy_end_time, greedy_start_time, result = greedy()

greedy_time = greedy_end_time - greedy_start_time


with open(f"../Results/algorithm-times.csv", "w") as f:
    print(f"BFS, {bfs_time}", file=f)
    print(f"DFS, {dfs_time}", file=f)
    print(f"GREEDY, {greedy_time}", file=f)
