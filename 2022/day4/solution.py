from aocd.models import Puzzle

puzzle = Puzzle(2022, 4)


def load_input_data():
    try:
        with open("input.txt") as f:
            input_data = f.read()
    except OSError:
        input_data = puzzle.input_data
        with open("input.txt", "x") as f:
            f.write(input_data)

    return input_data


def solve_a():
    ranges = load_input_data().splitlines()

    pairs = 0
    for range in ranges:
        pair1, pair2 = range.split(",")

        a1, b1 = map(int, pair1.split("-"))
        a2, b2 = map(int, pair2.split("-"))

        # Check fully contained pairs
        if (a1 <= a2 and b1 >= b2): pairs += 1
        elif (a2 <= a1 and b2 >= b1): pairs += 1

    return pairs


def solve_b():
    ranges = load_input_data().splitlines()

    pairs = 0
    for range in ranges:
        pair1, pair2 = range.split(",")

        a1, b1 = map(int, pair1.split("-"))
        a2, b2 = map(int, pair2.split("-"))

        # Check partially contained pairs
        if (a1 <= a2 and b1 >= a2): pairs += 1
        elif (a2 <= a1 and b2 >= a1): pairs += 1

    return pairs



puzzle.answer_a = solve_a()
puzzle.answer_b = solve_b()
