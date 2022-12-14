from aocd.models import Puzzle


from pprint import pprint
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

    num_dirs = 0
    for line in lines[1:]:
        if line == "$ ls": continue
        if line.startswith("$ cd"):
            dirname = line.split()[-1]

            if dirname == "..": path.pop()
            else:
                path.append(dirname)
                if not cur_dir.get(dirname): 
                    cur_dir[dirname] = {}
                    dir_sizes[dirname] = 0
            
            # Load the current directory
            cur_dir = load_dir(path)

        elif line.startswith("dir"):
            # Process subdirectory
            dirname = line.split()[-1]

            if not dir_sizes.get(dirname): dir_sizes[dirname] = 0
            if not cur_dir.get(dirname): 
                cur_dir[dirname] = {}
                
            num_dirs +=1
        
        else:
            # Process files
            size, filename = line.split()
            cur_dir[filename] = int(size)

            # Add file size for relevant directories
            for dir in path: dir_sizes[dir] += int(size)
        

    pprint(dir_sizes)
    # Sum all directories < 100,000
    sum_sizes = 0
    for _, size in dir_sizes.items():
        if size <= 100_000: sum_sizes += size

    print(num_dirs, len(dir_sizes.keys()))
    return sum_sizes


example_data = load_example_data()





# assert solve_a(example_data) == 95437

# puzzle.answer_a = solve_a() 1038055

solve_a()

