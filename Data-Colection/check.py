import os


def check_results_directory():
    if not os.path.exists("../Results"):
        os.makedirs("../Results")
