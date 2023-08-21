from bisect import insort


def a_star_add(gamesToProcess, newGame):
    insort(gamesToProcess, newGame)  # insert in a sorted way
