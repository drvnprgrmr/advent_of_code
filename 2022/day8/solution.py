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


def solve_b(data=None):
    if data == None: data = load_input_data()

    grid = [ [int(t) for t in row] for row in data.splitlines()]
    grid_len = len(grid)

    max_scenic_score = 0

    def scenic_score(grid, pos_y, pos_x):
        # Viewing distances in all directions
        top = 0
        bottom = 0
        left = 0
        right = 0
        
        val = grid[pos_y][pos_x]

        # Check above the tree
        for i in range(1, grid_len):
            # Check if you're off the grid
            if pos_y - i < 0: break

            top += 1
            comp = grid[pos_y - i][pos_x]

            if comp >= val: break

        # Check below the tree
        for i in range(1, grid_len):
            # Check if you're off the grid
            if pos_y + i == grid_len: break

            bottom += 1
            comp = grid[pos_y + i][pos_x]

            if comp >= val: break
            

        # Check to the left of the tree
        for i in range(1, grid_len):
            # Check if you're off the grid
            if pos_x - i < 0: break

            left += 1
            comp = grid[pos_y][pos_x - i]

            if comp >= val: break
        
        # Check to the right of the tree
        for i in range(1, grid_len):
            # Check if you're off the grid
            if pos_x + i == grid_len: break

            right += 1
            comp = grid[pos_y][pos_x + i]

            if comp >= val: break

        return top * bottom * left * right

    # Find the max of all scenic scores
    for y in range(grid_len):
        for x in range(grid_len):
            score = scenic_score(grid, y, x)
            if  score > max_scenic_score: max_scenic_score = score


    return max_scenic_score



# Example data
data = \
"""30373
25512
65332
33549
35390
"""

assert solve_a(data) == 21
assert solve_b(data) == 8

puzzle.answer_a = solve_a()
puzzle.answer_b = solve_b()
