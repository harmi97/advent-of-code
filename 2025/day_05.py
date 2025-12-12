"""Advent of Code solution of Year 2025 Day 5."""

from copy import deepcopy
from pathlib import Path

DATA = Path(__file__.replace(".py", ".txt")).read_text()


def part1(ranges: list[tuple[int, int]], items: list[int]):
    fresh_items = 0
    for item in items:
        valid_range = [item for r in ranges if r[0] <= item <= r[1]]
        fresh_items += 1 if valid_range else 0

    print(f"Part 1  = {fresh_items}")


def part2(ranges: list[tuple[int, int]]):
    ranges = set(ranges)
    new_ranges = deepcopy(ranges)
    while True:
        updated = False
        for rng1 in ranges:
            for rng2 in ranges:
                if rng2[0] <= rng1[0] <= rng2[1] and rng2 != rng1:
                    flattened = [r2 for r1 in [rng1, rng2] for r2 in r1]
                    min_val = min(flattened)
                    max_val = max(flattened)
                    # Range could already be removed by previous iteration
                    try:
                        new_ranges.remove(rng2)
                    except KeyError:
                        pass
                    try:
                        new_ranges.remove(rng1)
                    except KeyError:
                        pass
                    new_ranges.add((min_val, max_val))
                    updated = True
                    break
        ranges = deepcopy(new_ranges)
        if not updated:
            break
    fresh_items = [(r[1] - r[0]) + 1 for r in ranges]
    print(f"Part 2  = {sum(fresh_items)}")


if __name__ == "__main__":
    data = DATA.split("\n\n")
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in data[0].split("\n")]
    items = [int(i) for i in data[1].split("\n")]

    part1(ranges, items)
    part2(ranges)
