"""Advent of Code solution of Year 2025 Day 6."""

import math
from pathlib import Path

DATA = Path(__file__.replace(".py", ".txt")).read_text()
MAX_DIGITS = 4


def part1(data: list[list[str]]):
    data = [[r1 for r1 in r0.strip(" ").split((" ")) if r1 != ""] for r0 in data]
    results = []
    max_cols = len(data[0])
    max_rows = len(data) - 1
    for idx_c in range(max_cols):
        numbers = [int(data[idx_r][idx_c]) for idx_r in range(max_rows)]
        op = data[-1][idx_c]
        if op == "+":
            results.append(sum(numbers))
        if op == "*":
            results.append(math.prod(numbers))

    print(f"Part 1  = {sum(results)}")


def part2(data: list[list[str]]):
    data = tuple(reversed(line) for line in data)
    operator = None
    numbers = []
    results = []
    for row in zip(*data):
        try:
            numbers.append(int("".join(row[:-1])))
        except ValueError:  # New row
            numbers = []
            continue
        operator = row[-1]
        if operator == "+":
            results.append(sum(numbers))
        if operator == "*":
            results.append(math.prod(numbers))

    print(f"Part 2  = {sum(results)}")


if __name__ == "__main__":
    data = DATA.splitlines()
    part1(data)
    part2(data)
