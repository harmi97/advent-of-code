"""Advent of Code solution of Year 2024 Day 3."""

import re
from pathlib import Path


def read_file():
    with open(Path(Path(__file__).parent, "3.txt")) as f:
        data = f.readlines()
    return "".join(x.rstrip() for x in data)


def part1(data):
    data = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data)
    mul_sum = 0
    for d in data:
        d = re.findall(r"[0-9]{1,3}", d)
        mul_sum += int(d[0]) * int(d[1])
    return mul_sum


def part2(data):
    do_parts = re.sub(
        r"(don't\(\).*?do\(\)|don't\(\).*?$)",
        "",
        data,
    )
    return part1(do_parts)


if __name__ == "__main__":
    result = read_file()
    print(f"Part 1: result = {part1(result)}")
    print(f"Part 2: result = {part2(result)}")
