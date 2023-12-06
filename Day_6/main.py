from pathlib import Path
from typing import Dict, List
import re

_ROOT = Path(__file__).resolve().parents[0]


def read_puzzle_input(filename):
    with open(Path(_ROOT, "data", filename), "r") as f:
        puzzle_input = f.read().splitlines()
    return puzzle_input


def parse_puzzle_input(puzzle_input: List) -> List[Dict]:
    parsed_puzzle_input: List = []
    race_times = [int(item) for item in re.findall(r"[0-9]+", puzzle_input[0])]
    record_distances = [int(item) for item in re.findall(r"[0-9]+", puzzle_input[1])]
    for race_id, (race_time, record_distance) in enumerate(
        zip(race_times, record_distances)
    ):
        race_details: Dict = dict(
            race_id=race_id, race_time=race_time, record_distance=record_distance
        )
        parsed_puzzle_input.append(race_details)
    return parsed_puzzle_input


def parse_puzzle_input_part2(puzzle_input: List) -> List[Dict]:
    parsed_puzzle_input: List = []
    race_time = [int(puzzle_input[0].split(":")[-1].replace(" ", ""))]
    record_distance = [int(puzzle_input[1].split(":")[-1].replace(" ", ""))]
    for race_id, (race_time, record_distance) in enumerate(
        zip(race_time, record_distance)
    ):
        race_details: Dict = dict(
            race_id=race_id, race_time=race_time, record_distance=record_distance
        )
        parsed_puzzle_input.append(race_details)
    return parsed_puzzle_input


def calculate_winning_button_durations(race_data: Dict) -> None:
    winning_milli_durations: List = []
    for hold_button_millisecond in range(1, race_data["race_time"] + 1):
        distance_travelled = hold_button_millisecond * (
            race_data["race_time"] - hold_button_millisecond
        )
        if distance_travelled > race_data["record_distance"]:
            winning_milli_durations.append(hold_button_millisecond)
    race_data["wining_hold_durations"] = winning_milli_durations


def execute(filename: str):
    puzzle_input = read_puzzle_input(filename)
    parsed_input_part_1 = parse_puzzle_input(puzzle_input)
    parsed_input_part_2 = parse_puzzle_input_part2(puzzle_input)
    for race in parsed_input_part_1:
        calculate_winning_button_durations(race)

    part_1 = 1
    for race in parsed_input_part_1:
        part_1 *= len(race["wining_hold_durations"])

    for race in parsed_input_part_2:
        calculate_winning_button_durations(race)

    part_2 = 1
    for race in parsed_input_part_2:
        part_2 *= len(race["wining_hold_durations"])

    return part_1, part_2


if __name__ == "__main__":
    # print(f"Output: {execute('test_input.txt')}")
    print(f"Output: {execute('input.txt')}")
