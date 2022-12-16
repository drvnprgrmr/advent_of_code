from aocd.models import Puzzle

from os import path


puzzle = Puzzle(2022, 8)

def load_input_data():
    try:
        with open(path.join(path.dirname(__file__), "input.txt")) as f:
            input_data = f.read()
    except FileNotFoundError:
        input_data = puzzle.input_data
        with open(path.join(path.dirname(__file__), "input.txt"), "x") as f:
            f.write(input_data)

    return input_data



def solve_a(data=None):
    if data == None: data = load_input_data()

    forest_grid = [[ int(height) for height in row] for row in data.splitlines()]
    visible_grid = [[False for _ in row] for row in data.splitlines()]

    grid_len = len(forest_grid[0])

    from pprint import pprint

    # Check from LEFT to RIGHT
    for y, row in enumerate(forest_grid):
        tallest = -1
        for x, height in enumerate(row):
            if height > tallest:
                tallest = int(height)
                if not visible_grid[y][x]: visible_grid[y][x] = True


    # Check from RIGHT to LEFT
    for y, row in enumerate(forest_grid):
        tallest = -1
        for x, height in enumerate(reversed(row)):
            if height > tallest:
                tallest = int(height)
                if not visible_grid[y][grid_len-x-1]: visible_grid[y][grid_len-x-1] = True

    # Check from TOP to BOTTOM
    for x in range(grid_len):
        tallest = -1
        for y in range(grid_len):
            height = forest_grid[y][x]
            if height > tallest:
                tallest = int(height)
                if not visible_grid[y][x]: visible_grid[y][x] = True

    
    # Check from BOTTOM to TOP
    for x in range(grid_len):
        tallest = -1
        for y in range(grid_len):
            height = forest_grid[grid_len-y-1][x]
            if height > tallest:
                tallest = int(height)
                if not visible_grid[grid_len-y-1][x]: visible_grid[grid_len-y-1][x] = True
                
    pprint(forest_grid)
    pprint(visible_grid)


# Example data
data = \
"""30373
25512
65332
33549
35390
"""

solve_a(data)
