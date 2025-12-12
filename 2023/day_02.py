"""Advent of Code solution of Year 2023 Day 2."""

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


def part2_solution():
    lines = read_file()
    game_powers = []
    for line in lines:
        max_dice = {"red": 1, "green": 1, "blue": 1}
        dices = re.findall(r"(?P<count>\d*) (?P<dice>blue|green|red)", line)
        for dice in dices:
            dice_count, dice_color = dice
            dice_count = int(dice_count)
            if max_dice[dice_color] < dice_count:
                max_dice[dice_color] = dice_count
        game_power = max_dice["red"] * max_dice["blue"] * max_dice["green"]
        game_powers.append(game_power)
    print(f"Part 2 result = {sum(game_powers)}")


if __name__ == "__main__":
    part1_solution()
    part2_solution()
