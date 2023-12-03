from pathlib import Path
from collections import defaultdict

_ROOT = Path(__file__).resolve().parents[0]


def _get_numbers(row, row_start_idx, row_end_idx, grid_row_length, grid_line_length):
    number_set = set()
    for j in range(row_start_idx, row_end_idx):
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if (di, dj) == (0, 0):
                    continue
                nbri, nbrj = row + di, j + dj
                if 0 <= nbri < grid_row_length and 0 <= nbrj < grid_line_length:
                    number_set.add((nbri, nbrj))
    return number_set


def _is_symbol(char):
    return (not char.isdigit()) and char != "."


def execute(filename: str):
    running_total = 0
    table = defaultdict(list)
    with open(Path(_ROOT, "data", filename), "r") as f:
        grid = f.read().splitlines()
        grid_row_length = len(grid)
        grid_line_length = len(grid[0])

        for row in range(grid_row_length):
            row_idx = 0
            while row_idx < grid_row_length:
                if not grid[row][row_idx].isdigit():
                    row_idx += 1
                    continue
                second_row_idx = row_idx + 1
                while (
                    second_row_idx < grid_line_length
                    and grid[row][second_row_idx].isdigit()
                ):
                    second_row_idx += 1
                if any(
                    _is_symbol(grid[nbri][nbrj])
                    for nbri, nbrj in _get_numbers(
                        row, row_idx, second_row_idx, grid_row_length, grid_line_length
                    )
                ):
                    num = int(grid[row][row_idx:second_row_idx])
                    running_total += num
                    for nbri, nbrj in _get_numbers(
                        row, row_idx, second_row_idx, grid_row_length, grid_line_length
                    ):
                        if grid[nbri][nbrj] == "*":
                            table[(nbri, nbrj)].append(num)
                row_idx = second_row_idx

    gear_ratio = 0
    for v in table.values():
        if len(v) == 2:
            gear_ratio += v[0] * v[1]

    return running_total, gear_ratio


if __name__ == "__main__":
    print(f"Output: {execute('input.txt')}")
