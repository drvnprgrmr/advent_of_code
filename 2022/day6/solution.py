from aocd.models import Puzzle

puzzle = Puzzle(2022, 6)

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

def solve_a(data=None):
    if not data: data_stream = list(load_input_data())
    else: data_stream = list(data)

    start_of_packet = data_stream[:4]
    
    index = 4
    for packet in data_stream[4:]:
        condition = all([start_of_packet.count(p) == 1 for p in start_of_packet])

        if condition: break

        start_of_packet.pop(0)
        start_of_packet.append(packet)

        index += 1
    return index



def solve_b(data=None):
    if not data: data_stream = list(load_input_data())
    else: data_stream = list(data)

    start_of_message = data_stream[:14]
    
    index = 14
    for packet in data_stream[14:]:
        condition = all([start_of_message.count(p) == 1 for p in start_of_message])

        if condition: break

        start_of_message.pop(0)
        start_of_message.append(packet)

        index += 1
    return index


# Test to make sure the example works
example_data = load_example_data()
assert solve_a(example_data) == 7

puzzle.answer_a = solve_a()
puzzle.answer_b = solve_b()

