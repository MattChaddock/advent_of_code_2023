from pathlib import Path

_ROOT = Path(__file__).resolve().parents[0]


def execute(filename: str):
    running_total = 0

    with open(Path(_ROOT, "data", filename), "r") as f:
        lines = f.read().splitlines()
        numbers_list = [list(filter(str.isdigit, line)) for line in lines]
        for numbers in numbers_list:
            number = f"{numbers[0]}{numbers[-1]}"
            running_total += int(number)

    return running_total


if __name__ == "__main__":
    print(f"Output: {execute('input.txt')}")
