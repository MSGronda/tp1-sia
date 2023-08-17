import csv
import pandas as pd
import plotly.express as px
import check
from Algorithms import greedy, a_star

from Algorithms.Heuristics.manhattan_distance import calculate_manhattan_distance
from Algorithms.Heuristics.euclidian_distance import calculate_euclidian_distance
from Algorithms.Heuristics.average_distance import calculate_average_distance


check.check_results_directory()

board = "../Boards/board_benchmark.txt"
ITERATIONS = 10

# heuristics = ['manhattan', 'euclidian', 'average']
# algorithms = ['']

with open(f"../Results/heuristic-comparison.csv", "w") as f:
    print("With Manhattan")
    print("Running Greedy")
    for _ in range(ITERATIONS):
        greedy_end_time, greedy_start_time, result = greedy.greedy(board, calculate_manhattan_distance)
        greedy_time = greedy_end_time - greedy_start_time
        print(f"Manhattan, GREEDY, {greedy_time}", file=f)

    print("Running A*")
    for _ in range(ITERATIONS):
        Astar_end_time, Astar_start_time, solution_exists, _, _, _ = a_star.a_star(board, calculate_manhattan_distance)

        Astar_time = Astar_end_time - Astar_start_time
        print(f"Manhattan, A_STAR, {Astar_time}", file=f)

    print("With Euclidian")
    print("Running Greedy")
    for _ in range(ITERATIONS):
        greedy_end_time, greedy_start_time, result = greedy.greedy(board, calculate_euclidian_distance)
        greedy_time = greedy_end_time - greedy_start_time
        print(f"Euclidian, GREEDY, {greedy_time}", file=f)

    print("Running A*")
    for _ in range(ITERATIONS):
        Astar_end_time, Astar_start_time, solution_exists, _, _, _ = a_star.a_star(board, calculate_euclidian_distance)

        Astar_time = Astar_end_time - Astar_start_time
        print(f"Euclidian, A_STAR, {Astar_time}", file=f)

    print("With Average")
    print("Running Greedy")
    for _ in range(ITERATIONS):
        greedy_end_time, greedy_start_time, result = greedy.greedy(board, calculate_average_distance)
        greedy_time = greedy_end_time - greedy_start_time
        print(f"Average, GREEDY, {greedy_time}", file=f)

    print("Running A*")
    for _ in range(ITERATIONS):
        Astar_end_time, Astar_start_time, solution_exists, _, _, _ = a_star.a_star(board, calculate_average_distance)

        Astar_time = Astar_end_time - Astar_start_time
        print(f"Average, A_STAR, {Astar_time}", file=f)

data = []
with open(f"../Results/heuristic-comparison.csv", "r") as heuristics_data:
    reader = csv.reader(heuristics_data)
    for heuristic, algorithm, time in reader:
        data.append([heuristic, algorithm, float(time)])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Heuristic', 'Algorithm', 'Time'])

# Calculate the average and standard deviation for each group
grouped = df.groupby(['Heuristic', 'Algorithm']).agg({'Time': ['mean', 'std', 'count']})
grouped.columns = ['Mean', 'Std', 'Count']
grouped['Error'] = grouped['Std'] / grouped['Count']

# Reset the index
grouped.reset_index(inplace=True)

# Create the bar chart
fig = px.bar(grouped, x='Heuristic', y='Mean', color='Algorithm', error_y='Error', barmode='group',
             title='Comparison of Algorithms by Heuristic', text='Mean')
fig.update_layout(xaxis_title='Heuristic', yaxis_title='Time (s)', legend_title='Algorithm')
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')  # Show values on the bars
fig.show()
