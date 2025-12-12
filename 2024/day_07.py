"""Advent of Code solution of Year 2024 Day 7."""

import re
from itertools import product
from operator import add, concat, mul
from pathlib import Path

from tqdm import tqdm

OPERATORS_PART1 = (add, mul)
OPERATORS_PART2 = (add, mul, concat)


def read_file():
    with open(Path(Path(__file__).parent, "7.txt")) as f:
        lines = f.readlines()
    return [re.findall(r"[0-9]{1,}", line) for line in lines]


def solve(data, operators):
    result = 0
    for row in tqdm(data):
        expected_result = int(row[0])
        ops_combinations = product(operators, repeat=len(row[1:]) - 1)
        is_valid = False
        for ops in ops_combinations:
            for i, val in enumerate(row[1:]):
                if i == 0:
                    prev_value = int(val)
                    continue
                if ops[i - 1] == concat:
                    prev_value = int(ops[i - 1](str(prev_value), str(val)))
                else:
                    prev_value = ops[i - 1](int(prev_value), int(val))
                if prev_value > expected_result:
                    break
                if prev_value == expected_result:
                    is_valid = True
                    break
            if is_valid:
                result += expected_result
                break
    return result


if __name__ == "__main__":
    data = read_file()
    print(f"Part 1 result = {solve(data, OPERATORS_PART1)}")
    print(f"Part 2 result = {solve(data, OPERATORS_PART2)}")
