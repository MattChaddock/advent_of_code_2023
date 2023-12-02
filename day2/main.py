from pathlib import Path
import re

_ROOT = Path(__file__).resolve().parents[0]
RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

GAME_NUMBER_RE_PATTERN = r"^Game (\d+):"
CUBE_COLOUR_RE_PATTERN = r"(\d+) (red|green|blue)"


def execute(filename: str):
    running_total = 0
    power_total = 0
    with open(Path(_ROOT, "data", filename), "r") as f:
        for game in f.read().splitlines():
            min_red = 1
            min_green = 1
            min_blue = 1
            possible = True
            game_number = int(re.findall(GAME_NUMBER_RE_PATTERN, game)[0])
            game_rounds = game.split(":")[1:]
            rounds = "".join(game_rounds).split(";")
            for round in rounds:
                cubes = round.strip().split(",")
                for cube_set in cubes:
                    matches = re.findall(CUBE_COLOUR_RE_PATTERN, cube_set)
                    count, colour = matches[0]
                    count = int(count)
                    match colour:
                        case "red":
                            if count > RED_MAX:
                                possible = False
                            if count > min_red:
                                min_red = count
                        case "green":
                            if count > GREEN_MAX:
                                possible = False
                            if count > min_green:
                                min_green = count
                        case "blue":
                            if count > BLUE_MAX:
                                possible = False
                            if count > min_blue:
                                min_blue = count
            if possible:
                running_total += int(game_number)
            power = min_red * min_green * min_blue
            power_total += power
    return running_total, power_total


if __name__ == "__main__":
    print(f"Output: {execute('input.txt')}")
