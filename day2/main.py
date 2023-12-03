import re
from pathlib import Path

INPUT_FILE_PATH = Path(Path(__file__).parent, "input.txt")
CUBE_MAP = {"red": 12, "green": 13, "blue": 14}


def read_file():
    with open(INPUT_FILE_PATH, newline="") as f:
        lines = f.readlines()
    return lines


def part1_solution():
    lines = read_file()
    valid_game_ids = []
    for line in lines:
        valid_game = False
        game_id = re.match(r"Game (?P<game_id>\d*)", line).groupdict()["game_id"]
        dices = re.findall(r"(?P<count>\d*) (?P<dice>blue|green|red)", line)
        for dice in dices:
            dice_count, dice_color = dice
            valid_game = int(dice_count) <= CUBE_MAP[dice_color]
            if not valid_game:
                break
        if valid_game:
            valid_game_ids.append(int(game_id))
    print(f"Part 1 result = {sum(valid_game_ids)}")


if __name__ == "__main__":
    part1_solution()
