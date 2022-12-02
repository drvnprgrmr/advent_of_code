from aocd.models import Puzzle

puzzle = Puzzle(2022,2)

def parse():
    input_data = None

    try:
        with open("input.txt") as f:
            input_data = f.read()
    except OSError:
        input_data = puzzle.input_data
        with open("input.txt", "x") as f:
            f.write(input_data)


    return input_data



