from pathlib import Path
from enum import Enum

_ROOT = Path(__file__).resolve().parents[0]


class CubeColourCount(Enum):
    red = 12
    green = 13
    blue = 14


def read_puzzle_input(filename):
    with open(Path(_ROOT, "data", filename), "r") as f:
        puzzle_input = f.read().splitlines()
    return puzzle_input


def parse_game_results(games_data):
    parsed_results = {}
    for game_data in games_data:
        revealed_data = game_data.split(":")[-1].split(";")
        revealed_cube_data = []
        for data in revealed_data:
            cube_data = data.strip().split(",")
            mapped_data = {}
            for item in cube_data:
                cube_color = item.split()[-1]
                cube_count = int(item.split()[0])
                mapped_data[cube_color] = cube_count
            revealed_cube_data.append(mapped_data)
        parsed_results[int(game_data.split(":")[0].replace("Game ", ""))] = {
            "reveal_data": revealed_cube_data,
            "game_possible": None,
        }
    return parsed_results


def check_game_results_possible(games_data):
    for game_id, game_data in games_data.items():
        try:
            for reveal in game_data["reveal_data"]:
                for cube_colour, cube_count in reveal.items():
                    assert cube_count <= CubeColourCount[cube_colour].value
        except Exception:
            games_data[game_id]["game_possible"] = False
        else:
            games_data[game_id]["game_possible"] = True
    return games_data


def check_fewest_dice_possible(games_data):
    for game_id, game_data in games_data.items():
        red_cube_counts = []
        green_cube_counts = []
        blue_cube_counts = []

        for reveal in game_data["reveal_data"]:
            for cube_colour, cube_count in reveal.items():
                match cube_colour:
                    case "red":
                        red_cube_counts.append(cube_count)
                    case "green":
                        green_cube_counts.append(cube_count)
                    case "blue":
                        blue_cube_counts.append(cube_count)

        games_data[game_id]["min_red_cubes"] = max(red_cube_counts)
        games_data[game_id]["min_green_cubes"] = max(green_cube_counts)
        games_data[game_id]["min_blue_cubes"] = max(blue_cube_counts)
        games_data[game_id]["power"] = (
            games_data[game_id]["min_red_cubes"]
            * games_data[game_id]["min_green_cubes"]
            * games_data[game_id]["min_blue_cubes"]
        )

    return games_data


def calculate_possible_games(games_data):
    possible_games = [
        game_id
        for game_id, game_data in games_data.items()
        if game_data["game_possible"]
    ]
    return sum(possible_games)


def calculate_game_power(games_data):
    games_powers = [game_data["power"] for game_id, game_data in games_data.items()]
    return sum(games_powers)


def execute(filename: str):
    puzzle_input = read_puzzle_input(filename)
    parsed_game_results = parse_game_results(puzzle_input)
    game_validity = check_game_results_possible(parsed_game_results)
    game_power = check_fewest_dice_possible(parsed_game_results)
    part_1_answer = calculate_possible_games(game_validity)
    part_2_answer = calculate_game_power(game_power)
    print(f"Part 1 result is: {part_1_answer}")
    print(f"Part 2 result is: {part_2_answer}")
    return part_1_answer, part_2_answer


if __name__ == "__main__":
    print(f"Output: {execute('input.txt')}")
