from pathlib import Path

_ROOT = Path(__file__).resolve().parents[0]


def read_puzzle_input(filename):
    with open(Path(_ROOT, "data", filename), "r") as f:
        puzzle_input = f.read().splitlines()
    return puzzle_input


def execute(filename: str):
    pass


if __name__ == "__main__":
    print(f"Output: {execute('test_input.txt')}")
    print(f"Output: {execute('input.txt')}")
