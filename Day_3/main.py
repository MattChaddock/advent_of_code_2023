import re
from pathlib import Path
from typing import Dict, List, Tuple

_ROOT = Path(__file__).resolve().parents[0]


def read_puzzle_input(filename):
    with open(Path(_ROOT, "data", filename), "r") as f:
        puzzle_input = f.read().splitlines()
    return puzzle_input


def get_row_number_cords(grid_row: str) -> Dict:
    numbers: List = re.findall(r"[0-9]+", grid_row)
    number_coordinates: Dict = {}
    for number in numbers:
        number_coordinates[number] = [
            (match.start(), match.end() - 1) for match in re.finditer(number, grid_row)
        ]
    return number_coordinates


def check_for_adjacent_symbols(grid: List, grid_row: int, coordinates: List[Tuple]):
    # grid_rows = range(0, len(grid)-1)
    # grid_width = range(0, len(grid[0])-1)
    #
    # # [0, -1]   North
    # # # [1, 0]    East
    # # # [0, 1]    South
    # # # [-1, 0]   West
    # # # [1, -1]   North East
    # # # [1, 1]    South East
    # # # [-1, 1]   South West
    # # # [-1, -1]  North West
    #
    print(coordinates)
    cordys = []
    for cord in range(coordinates[0][0], coordinates[0][-1] + 1):
        cordys.append((coordinates[0][0], coordinates[0][0] + cord))

    # match grid_row:
    #     case 0:
    #         # First row, don't check to the North
    #         # # [1, 0]    East
    #         # # [0, 1]    South
    #         # # [-1, 0]   West
    #         # # [1, 1]    South East
    #         # # [-1, 1]   South West
    #         for direction in directions
    #         pass
    #
    #     case last_row if grid_row == len(grid_rows):
    #         # Last row, don't check to the South
    #         # [0, -1]   North
    #         # # [1, 0]    East
    #         # # [-1, 0]   West
    #         # # [1, -1]   North East
    #         # # [-1, -1]  North West
    #         pass
    #
    #     case _:
    #         # Check all directions
    #         # [0, -1]   North
    #         # # [1, 0]    East
    #         # # [0, 1]    South
    #         # # [-1, 0]   West
    #         # # [1, -1]   North East
    #         # # [1, 1]    South East
    #         # # [-1, 1]   South West
    #         # # [-1, -1]  North West
    #         pass


def _is_symbol(char):
    return (not char.isdigit()) and char != "."


def get_part_numbers(puzzle_input: List):
    # Build a map of the numbers on every grid row, and record each numbers coordinates
    grid_number_coordinates = {}
    for row_num, row_data in enumerate(puzzle_input):
        grid_number_coordinates[row_num] = get_row_number_cords(row_data)

    part_numbers: List = []
    for grid_row, number_coordinates in grid_number_coordinates.items():
        if number_coordinates:
            for number, coordinates in number_coordinates.items():
                print(number, coordinates)
                if check_for_adjacent_symbols(puzzle_input, grid_row, coordinates):
                    pass
                #     part_numbers.append(number)


def execute(filename: str):
    parsed_puzzle_data = read_puzzle_input(filename)
    get_part_numbers(parsed_puzzle_data)


if __name__ == "__main__":
    execute("test_input.txt")
    # print(f"Output: {execute('test_input.txt')}")
    # print(f"Output: {execute('input.txt')}")
