from aocd.models import Puzzle

from os import path


puzzle = Puzzle(2022, 7)

def load_input_data():
    try:
        with open(path.join(path.dirname(__file__), "input.txt")) as f:
            input_data = f.read()
    except FileNotFoundError:
        input_data = puzzle.input_data
        with open(path.join(path.dirname(__file__), "input.txt"), "x") as f:
            f.write(input_data)

    return input_data

def load_example_data():
    try:
        with open(path.join(path.dirname(__file__), "example.txt")) as f:
            example_data = f.read()
    except FileNotFoundError:
        example_data = puzzle.example_data
        with open(path.join(path.dirname(__file__), "example.txt"), "x") as f:
            f.write(example_data)

    return example_data


def solve_a(data=None):
    # PS: I feel like there's a better way to solve this
    # I'm just happy I finally found the solution
    if (data == None): data = load_input_data()
    
    lines = data.splitlines()

    dir_sizes = {"/": 0}
    structure = {"/": {}}


    path = ["/"]
    cur_dir = structure["/"]

    def load_dir(path):
        dir = structure["/"]
        for l in path[1:]:
            dir = dir[l]
        return dir


    lines = list(filter(lambda x: (not x == "$ ls") and (not x.startswith("dir")), lines))

    # Preprocess the lines by giving each file and folder
    # unique ids
    for i, line in enumerate(lines[:]):
        if line == "$ cd ..": continue
        if line.startswith("$ cd"): 
            lines[i] = lines[i] + f"_d{i}"
        else: 
            lines[i] = lines[i] + f"_f{i}"
    

    for line in lines[1:]:
        if line.startswith("$ cd"):
            dirname = line.split()[-1] 

            if dirname == "..": path.pop()
            else:
                path.append(dirname)

                # Check if dirname is not file
                if not type(cur_dir.get(dirname)) == dict:
                    cur_dir[dirname] = {}
                    dir_sizes[dirname] = 0
            
            # Load the current directory
            cur_dir = load_dir(path)
        
        else:
            # Process files
            size, filename = line.split()
            cur_dir[filename] = int(size)

            # Add file size for relevant directories
            for dir in path: dir_sizes[dir] += int(size)
        

    # Sum all directories < 100,000
    sum_sizes = 0
    for _, size in dir_sizes.items():
        if size <= 100_000: sum_sizes += size

    return sum_sizes, dir_sizes


def solve_b(dir_sizes):
    total_size = 70000000

    used_space = dir_sizes["/"]
    free_space = total_size - used_space

    space_needed = 30000000 - free_space

    for size in sorted(dir_sizes.values()):
        if size >= space_needed:
            return size
    




example_data = load_example_data()
assert solve_a(example_data) == 95437


puzzle.answer_a, dir_sizes = solve_a()
puzzle.answer_b = solve_b(dir_sizes)


# NOTE: This is a note to future self. 
# Refactore the code to first create the 
# directory structure and then calculate dir_sizes.
# As a tip you can add a `size: int` and `computed: boolean` field
# PS: Make sure the assertion does not fail.
