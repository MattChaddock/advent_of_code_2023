from pathlib import Path
from typing import List, Dict, Tuple
import re

_ROOT = Path(__file__).resolve().parents[0]


def read_puzzle_input(filename):
    with open(Path(_ROOT, "data", filename), "r") as f:
        puzzle_input = f.read().splitlines()
    return puzzle_input


def parse_puzzle_input(puzzle_input: List) -> Dict:
    parsed_puzzle_input: Dict = {}
    for scratchcard in puzzle_input:
        card_number = int(scratchcard.split("|")[0].split(":")[0].replace("Card ", ""))
        winning_numbers: List = re.findall(
            r"[0-9]+", scratchcard.split("|")[0].split(":")[1]
        )
        card_numbers: List = re.findall(r"[0-9]+", scratchcard.split("|")[1])
        parsed_puzzle_input[card_number] = {
            "winning_numbers": [int(_) for _ in winning_numbers],
            "card_numbers": [int(_) for _ in card_numbers],
            "card_copies": 0,
        }
    return parsed_puzzle_input


def calculate_card_score(card_data: Dict) -> Tuple[int, int]:
    matched_winning_numbers = frozenset(card_data["card_numbers"]).intersection(
        card_data["winning_numbers"]
    )
    card_score = (
        0
        if len(matched_winning_numbers) == 0
        else 2 ** (len(matched_winning_numbers) - 1)
    )
    return len(matched_winning_numbers), card_score


def calc_card_wins(parsed_puzzle_input: Dict) -> Tuple[int, int]:
    total_card_points = 0
    total_scratchcards = 0
    for card_number, card_data in parsed_puzzle_input.items():
        matched_count, card_score = calculate_card_score(card_data)
        parsed_puzzle_input[card_number].update(
            {"matched_count": matched_count, "card_score": card_score}
        )
        total_card_points += card_score
        for _ in range(1, matched_count + 1):
            parsed_puzzle_input[card_number + _]["card_copies"] += 1

        for _ in range(parsed_puzzle_input[card_number]["card_copies"]):
            for _ in range(1, matched_count + 1):
                parsed_puzzle_input[card_number + _]["card_copies"] += 1

    for value in parsed_puzzle_input.values():
        total_scratchcards += value["card_copies"] + 1

    return total_card_points, total_scratchcards


def execute(filename: str):
    parsed_puzzle_input = parse_puzzle_input(read_puzzle_input(filename))
    part1, part2 = calc_card_wins(parsed_puzzle_input)
    return part1, part2


if __name__ == "__main__":
    # print(f"Output: {execute('test_input.txt')}")
    print(f"Output: {execute('input.txt')}")
