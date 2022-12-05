from aocd.models import Puzzle

puzzle = Puzzle(2022, 3)


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


def solve_a():
    data = load_input_data()
    rucksacks = data.splitlines()

    cache = {}
    sum_priorities = 0

    for sack in rucksacks:
        mid = len(sack) / 2
        for i, char in enumerate(sack):
            if i < mid:
                cache[char] = True
            else:
                if cache.get(char, False):
                    if char.islower():
                        sum_priorities += ord(char) - 96
                    else: sum_priorities += ord(char) - 64 + 26
                    break

        cache.clear()

    return sum_priorities


def solve_b():
    data = load_input_data()
    rucksacks = data.splitlines()

    group = {}
    recorded = {}

    sum_priorities = 0

    for sack in rucksacks:
        for char in sack:
            if not recorded.get(char, False): 
                group[char] = group.get(char, 0) + 1
                if group[char] == 3: 
                    if char.islower():
                        sum_priorities += ord(char) - 96
                    else:
                        sum_priorities += ord(char) - 64 + 26
                    # Clear the group dict after every three loops
                    group.clear()
                    break
                recorded[char] = True
        # Reset the `recorded` dict after every loop
        recorded.clear()

    return sum_priorities



puzzle.answer_a = solve_a()
puzzle.answer_b = solve_b()