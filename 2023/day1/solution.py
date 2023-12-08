from aocd.models import Puzzle
from os import path

# Set the year and day for this puzzle
YEAR = 2023
DAY = 1


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

        lines = data.splitlines()
        calibration_value = 0

        for line in lines:
            # Find first digit
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break
            # Find last digit
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break

            calibration_value += int(first_digit + last_digit)

        if not self.puzzle.answered_a and not data:
            self.puzzle.answer_a = calibration_value
        return calibration_value

    def solve_b(self, data=None):
        """
        Solve the 'b' section of this puzzle.
        """
        if not data:
            data = self.data

        spelling_to_digit = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }
        lines = data.splitlines()
        calibration_value = 0

        for line in lines:
            digits = []
            spelled_out = []
            for char in line:
                spelled_out.append(char)

                for spelling in spelling_to_digit.keys():
                    if spelling in "".join(spelled_out):
                        digits.append(spelling_to_digit[spelling])
                        spelled_out.clear()

                if char.isdigit():
                    digits.append(char)
                    spelled_out.clear()
            calibration_value += int(digits[0] + digits[-1])

        if not self.puzzle.answered_b and not data:
            self.puzzle.answer_b = calibration_value
        print(calibration_value)
        return calibration_value

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
        p.solve_a()

    if p.test_b():
        p.solve_b()
