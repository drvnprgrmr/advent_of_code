from aocd.models import Puzzle

puzzle = Puzzle(2022, 2)


def load_input_data():
    input_data = None

    try:
        with open("input.txt") as f:
            input_data = f.read()
    except OSError:
        input_data = puzzle.input_data
        with open("input.txt", "x") as f:
            f.write(input_data)

    return input_data


def parse():
    data = load_input_data()

    return data.splitlines()


scores = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

outcomes = {
    # Draws
    "A X": 3,
    "B Y": 3,
    "C Z": 3,

    # Wins
    "C X": 6,
    "A Y": 6,
    "B Z": 6,
}

def solve_a():
    games = parse()


    score = 0
    for round in games:
        score += outcomes.get(round, 0) + scores[round[-1]]

    return score


def solve_b():
    games = parse()

    draw = {
        "A": "X",
        "B": "Y",
        "C": "Z",
    }

    win = {
        "A": "Y",
        "B": "Z",
        "C": "X",
    }

    lose = {
        "A": "Z",
        "B": "X",
        "C": "Y"
    }

    score = 0   
    for round in games:
        move, end_in = round.split()

        if (end_in == "X"):
            score += outcomes.get(f"{move} {lose[move]}", 0) + scores[lose[move]]
        elif (end_in == "Y"):
            score += outcomes.get(f"{move} {draw[move]}", 0) + scores[draw[move]]
        elif (end_in == "Z"):
            score += outcomes.get(f"{move} {win[move]}", 0) + scores[win[move]]

    return score


# Submit solutions
puzzle.answer_a = solve_a()
puzzle.answer_b = solve_b()