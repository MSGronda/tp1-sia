import csv
import pandas as pd
import plotly.express as px
import check
from Algorithms import greedy, a_star

from Algorithms.Heuristics.combined_heuristic import combined_heuristic
from Algorithms.Heuristics.lost_game import lost_game_heuristic
from Algorithms.Heuristics.manhattan_distance import calculate_manhattan_distance
from Algorithms.Heuristics.euclidian_distance import calculate_euclidian_distance
from Algorithms.Heuristics.average_distance import calculate_average_distance
from Algorithms.Heuristics.manhattan_wall_detection import calculate_manhattan_distance_wall_detection

check.check_results_directory()

board = "../Boards/board.txt"
ITERATIONS = 1

heuristic_array = [
    (calculate_manhattan_distance, 'manhattan'), (calculate_euclidian_distance, 'euclidian'), (calculate_average_distance, 'max (euclidian and manhattan)'),
    (calculate_manhattan_distance_wall_detection, 'manhattan-wall'), (lost_game_heuristic, 'lost-game'), (combined_heuristic, 'combined (manhattan and lost-game)')
]

with open(f"../Results/heuristic-comparison.csv", "w") as f:
    for heuristic, name in heuristic_array:
        print(f"With {name}")
        print("  Running Greedy")
        for _ in range(ITERATIONS):
            greedy_end_time, greedy_start_time, result = greedy.greedy(board, heuristic)
            greedy_time = greedy_end_time - greedy_start_time
            print(f"{name}, GREEDY, {greedy_time}", file=f)

        print("  Running A*")
        for _ in range(ITERATIONS):
            Astar_end_time, Astar_start_time, solution_exists, _, _, _ = a_star.a_star(board, heuristic)
            Astar_time = Astar_end_time - Astar_start_time
            print(f"{name}, A_STAR, {Astar_time}", file=f)



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
