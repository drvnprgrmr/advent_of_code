from aocd.models import Puzzle

puzzle = Puzzle(2022, 1)

# Get group data.
groups = [ [int(data) for data in group.split() ] for group in puzzle.input_data.split("\n\n")]


def solve_a():
    """ Find most calories """    
    max_sum = 0
    for group in groups:
        if sum(group) > max_sum: max_sum = sum(group)

    return max_sum

def solve_b():
    """ Find sum of top 3 most calories. """
    first = second = third = 0

    for group in groups:
        group_sum = sum(group)
        if group_sum > first: 
            second, first = first, group_sum
        if group_sum < first and group_sum > second: 
            third, second = second, group_sum
        if group_sum < second and group_sum > third: 
            third = group_sum

    return first + second + third


if __name__ == "__main__":
    # Submit solutions
    puzzle.answer_a = solve_a()
    puzzle.answer_b = solve_b()