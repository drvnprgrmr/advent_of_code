from aocd.models import Puzzle
from os import path

# Set the year and day for this puzzle
YEAR = 0  # Change this to the current puzzle year
DAY = 0   # Change this to the current puzzle day

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
        # Check if puzzle is solved
        if self.puzzle.answered_a:
            if __name__ == "__main__":
                print(f"Solution to a: {self.puzzle.answer_a}")

        if not data:
            data = self.data

        # TODO: Write algorithm here

    def solve_b(self, data=None):
        """
        Solve the 'b' section of this puzzle.
        """
        # Check if puzzle is solved
        if self.puzzle.answered_a:
            if __name__ == "__main__":
                print(f"Solution to a: {self.puzzle.answer_a}")

        if not data:
            data = self.data

        # TODO: Write algorithm here

    def test(self):
        examples = self.puzzle.examples

        all_passed = True

        for i, example in enumerate(examples):
            print(f"Testing Example #{i + 1}\n")
            print(f"Data:\n{example.input_data}\n")

            # Test solution a
            print("Testing Solution A")
            solved_b = self.solve_a(example.input_data)
            if solved_b == example.answer_a:
                print("Correct!", f"Answer is '{solved_b}'")
            else:
                all_passed = False
                print(
                    "Wrong!",
                    f"Correct answer is '{example.answer_a}'.",
                    f"Provided answer is '{solved_b}'.",
                )
            print()

            # Test solution b
            print("Testing Solution B")
            solved_b = self.solve_b(example.input_data)
            if solved_b == example.answer_b:
                print("Correct!", f"Answer is '{solved_b}'")
            else:
                all_passed = False
                print(
                    "Wrong!",
                    f"Correct answer is '{example.answer_b}'.",
                    f"Provided answer is '{solved_b}'.",
                )
            print()

        return all_passed

if __name__ == "__main__":
    p = MyPuzzle(YEAR, DAY)

    # If the test passes solve current day's challenge
    if p.test():
        p.solve_a()
        p.solve_a()

