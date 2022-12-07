from aocd.models import Puzzle
from pprint import pprint

puzzle = Puzzle(2022, 5)


def load_input_data():
    try:
        with open("input.txt") as f:
            input_data = f.read()
    except OSError:
        input_data = puzzle.input_data
        with open("input.txt", "x") as f:
            f.write(input_data)

    return input_data

def load_example_data():
    try:
        with open("example.txt") as f:
            example_data = f.read()
    except OSError:
        example_data = puzzle.example_data
        with open("example.txt", "x") as f:
            f.write(example_data)

    return example_data


def parse():
    data = load_input_data()
    stacks_str, moves_str = data.split("\n\n")

    # Parse moves
    moves = [
        [
            int(move.split()[1]),  # Count
            int(move.split()[3]),  # From
            int(move.split()[5])   # To
        ]
        for move in moves_str.split("\n")
    ]

    # Get everything except the number row and reverse it
    stacks_split = stacks_str.split("\n")[:-1]
    stacks_split.reverse()

    # Calculate the number of stacks
    num_stacks = int((len(stacks_split[0]) + 1) / 4)

    stacks = [[] for _ in range(num_stacks)]
    for row in stacks_split:
        for i in range(num_stacks):
            cur_crate = row[1 + i*4]
            if cur_crate != " ":
                stacks[i].append(cur_crate)
    
    return moves, stacks


def solve_a():
    moves, stacks = parse()
    for count, fro, to in moves:
        # Get values to perform operations
        stack_fro = stacks[fro - 1]
        stack_to = stacks[to - 1]

        removed = stack_fro[-count:]
        removed.reverse()  # Reverse `removed` because it is popped one at a time
        stack_fro = stack_fro[:-count]
        stack_to.extend(removed)

        # Set new values after operations
        stacks[fro - 1] = stack_fro
        stacks[to - 1] = stack_to

    # Get the top crate for each stack
    top_crates = "".join([stack[-1] for stack in stacks])
    return top_crates

def solve_b():
    """
    Only change to `solve_a` is to pick `count` all at
    once and not one at a time. 
    """
    moves, stacks = parse()
    for count, fro, to in moves:
        # Get values to perform operations
        stack_fro = stacks[fro - 1]
        stack_to = stacks[to - 1]

        # Pick all crates at once
        removed = stack_fro[-count:]

        stack_fro = stack_fro[:-count]
        stack_to.extend(removed)

        # Set new values after operations
        stacks[fro - 1] = stack_fro
        stacks[to - 1] = stack_to

    # Get the top crate for each stack
    top_crates = "".join([stack[-1] for stack in stacks])
    return top_crates


puzzle.answer_a = solve_a()
puzzle.answer_b = solve_b()