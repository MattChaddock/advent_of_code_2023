from pathlib import Path
import re

_ROOT = Path(__file__).resolve().parents[0]

NUMBER_PATTERN = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"

NUMBER_STRINGS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_number(value: str) -> int:
    if value.isdigit():
        return int(value)
    else:
        return NUMBER_STRINGS[value]


def execute(filename: str):
    running_total = 0

    with open(Path(_ROOT, "data", filename), "r") as f:
        lines = f.read().splitlines()
        lines = [re.findall(NUMBER_PATTERN, line) for line in lines]

        for line in lines:
            num1 = get_number(line[0])
            num2 = get_number(line[-1])
            number = f"{num1}{num2}"
            running_total += int(number)

    return running_total


if __name__ == "__main__":
    print(f"Output: {execute('input.txt')}")
