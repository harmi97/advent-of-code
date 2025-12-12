"""Advent of Code solution of Year 2025 Day 7."""

from copy import deepcopy
from pathlib import Path

DATA = Path(__file__.replace(".py", ".txt")).read_text()
SPLITTER = "^"
START = "S"


def part1(data: list[list[str]]):
    splitter_hits = 0
    beam_indexes = {data[0].index(START)}
    for line in data:
        if set(line) == {"."}:
            continue
        while True:
            try:
                splitter_idx = line.index(SPLITTER)
            except ValueError:
                break
            line[splitter_idx] = "X"
            # do not count if beam is not above
            if splitter_idx not in beam_indexes:
                continue
            splitter_hits += 1
            beam_indexes.remove(splitter_idx)
            beam_indexes.add(splitter_idx + 1)  # right
            beam_indexes.add(splitter_idx - 1)  # left
    print(f"Part 1  = {splitter_hits}")


def part2(data: list[list[str]]):
    START_POSITION = data[0].index(START)
    bean = [0] * len(data[0])
    bean[START_POSITION] = 1  # Initial bean
    beam_indexes = {START_POSITION}

    for line in data:
        if set(line) == {"."}:
            continue
        while True:
            try:
                splitter_idx = line.index(SPLITTER)
            except ValueError:
                break
            line[splitter_idx] = "X"
            # do not count if beam is not above
            if splitter_idx not in beam_indexes:
                continue

            beam_idx_left = splitter_idx - 1
            beam_idx_right = splitter_idx + 1
            beam_indexes.remove(splitter_idx)
            beam_indexes.add(beam_idx_right)  # right
            beam_indexes.add(beam_idx_left)  # left
            # If bean is split add previous beans variants and reset position
            bean[beam_idx_left] += bean[splitter_idx]
            bean[beam_idx_right] += bean[splitter_idx]
            bean[splitter_idx] = 0
    print(f"Part 2  = {sum(bean)}")


if __name__ == "__main__":
    data = DATA.splitlines()
    data = [list(r) for r in data]
    part1(deepcopy(data))
    part2(data)
