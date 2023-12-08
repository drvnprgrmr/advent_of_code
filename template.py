from aocd.models import Puzzle
from os import path

# Set the year and day for this puzzle
YEAR = 0  # Change this to the current puzzle year
DAY = 0  # Change this to the current puzzle day


class MyPuzzle:
    def __init__(self, year: int, day: int):
        self.puzzle = Puzzle(year, day)
        self.data = self.load_input_data()

    def load_input_data(self):
        """
        Load the input data for this puzzle from 'input.txt'.
        If 'input.txt' doesn't exist, create it and write input data to it.
        """
        try:
            with open(path.join(path.dirname(__file__), "input.txt")) as f:
                input_data = f.read()
        except FileNotFoundError:
            input_data = self.puzzle.input_data
            with open(path.join(path.dirname(__file__), "input.txt"), "x") as f:
                f.write(input_data)

        return input_data

    def solve_a(self, data=None):
        """
        Solve the 'a' section of this puzzle.
        """
        if not data:
            data = self.data

        # TODO: Write algorithm here

        if not self.puzzle.answered_a and not data:
            self.puzzle.answer_a = answer
        return answer

    def solve_b(self, data=None):
        """
        Solve the 'b' section of this puzzle.
        """
        if not data:
            data = self.data

        # TODO: Write algorithm here

        if not self.puzzle.answered_b and not data:
            self.puzzle.answer_b = answer
        return answer

    def test_a(self):
        example = self.puzzle.examples[0]
        passed = True

        print("Testing Solution A\n")

        print(f"Data:\n{example.input_data}\n")

        solved_a = self.solve_a(example.input_data)
        if str(solved_a) == example.answer_a:
            print("Correct!", f"Answer is '{solved_a}'")
        else:
            passed = False
            print(
                "Wrong!",
                f"Correct answer is '{example.answer_a}'.",
                f"Provided answer is '{solved_a}'.",
            )
        print()

        return passed

    def test_b(self):
        example = self.puzzle.examples[-1]
        passed = True

        print("Testing Solution B\n")

        print(f"Data:\n{example.input_data}\n")

        solved_b = self.solve_b(example.input_data)
        if str(solved_b) == example.answer_b:
            print("Correct!", f"Answer is '{solved_b}'")
        else:
            passed = False
            print(
                "Wrong!",
                f"Correct answer is '{example.answer_b}'.",
                f"Provided answer is '{solved_b}'.",
            )
        print()

        return passed


if __name__ == "__main__":
    p = MyPuzzle(YEAR, DAY)

    if p.test_a():
        print(f"Solution to A: {p.solve_a()}")

    if p.test_b():
        print(f"Solution to B: {p.solve_b()}")
