import matplotlib.pyplot as plt


def createHeuristicsGraph(data_to_plot):
    # Prepare data for plotting
    boards = list(data_to_plot.keys())
    heuristics = list(data_to_plot[boards[0]].keys())
    solution_steps = [[data_to_plot[board][heuristic] for heuristic in heuristics] for board in boards]

    # Create the bar chart
    fig, ax = plt.subplots()
    width = 0.2
    x = range(len(boards))

    for i, heuristic in enumerate(heuristics):
        ax.bar([pos + width * i for pos in x], [depths[i] for depths in solution_steps], width,
               label=f"Heuristic: {heuristic}")

    ax.set_xticks([pos + width for pos in x])
    ax.set_xticklabels(boards)
    ax.set_ylabel('Steps to reach goal board')
    ax.set_title('Comparison of Steps to reach goal for Different Heuristics')
    ax.legend()

    plt.show()