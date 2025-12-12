"""Advent of Code solution of Year 2023 Day 1."""

import re
from pathlib import Path

NUMBER_MAP = {
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
INPUT_FILE_PATH = Path(Path(__file__).parent, "input.txt")


def read_file():
    with open(INPUT_FILE_PATH, newline="") as f:
        lines = f.readlines()
    return lines


# Part 1
def solution_part1(lines):
    numbers = []
    for line in lines:
        digits = re.findall(r"[0-9]", line)
        if digits:
            numbers.append(int(digits[0] + digits[-1]))
    print(f"Part 1 result = {sum(numbers)}")


# Part 2
def solution_part2(lines):
    digits_str = f"(?=(\d|{'|'.join(NUMBER_MAP.keys())}))"
    numbers = []
    for line in lines:
        digits = re.findall(digits_str, line)
        if digits:
            first = convert_to_digit(digits[0])
            last = convert_to_digit(digits[-1])
            numbers.append(int(first + last))
    print(f"Part 2 result = {sum(numbers)}")


def convert_to_digit(x):
    try:
        return str(NUMBER_MAP[x])
    except KeyError:
        return x


if __name__ == "__main__":
    lines = read_file()
    solution_part1(lines)
    solution_part2(lines)
