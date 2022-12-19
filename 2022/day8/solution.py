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

    # Solve the grid in every direction
    for x in range(grid_len):
        tallest_top = -1
        tallest_right = -1
        tallest_bottom = -1
        tallest_left = -1
        for y in range(grid_len):
            height_top = forest_grid[y][x]
            height_right = forest_grid[x][grid_len-y-1]
            height_bottom = forest_grid[grid_len-y-1][x]
            height_left = forest_grid[x][y]
            if height_top > tallest_top:
                tallest_top = int(height_top)
                if not visible_grid[y][x]: visible_grid[y][x] = True
            if height_bottom > tallest_bottom:
                tallest_bottom = int(height_bottom)
                if not visible_grid[grid_len-y-1][x]:
                    visible_grid[grid_len-y-1][x] = True
            if height_left > tallest_left:
                tallest_left = int(height_left)
                if not visible_grid[x][y]:
                    visible_grid[x][y] = True
            if height_right > tallest_right:
                tallest_right = int(height_right)
                if not visible_grid[x][grid_len-y-1]:
                    visible_grid[x][grid_len-y-1] = True

                
    

    # Sum all True elements in the grid
    visible_trees = 0
    for _ in visible_grid:
        for t in _:
            if t: visible_trees += 1
    
    print(visible_trees)
    return visible_trees

# Example data
data = \
"""30373
25512
65332
33549
35390
"""

# assert solve_a(data) == 21

puzzle.answer_a = solve_a()