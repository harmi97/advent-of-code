"""Advent of Code solution of Year 2024 Day 8."""

from collections import defaultdict
from operator import add, sub
from pathlib import Path


def read_file():
    with open(Path(Path(__file__).parent, "8.txt")) as f:
        lines = f.readlines()
    return [list(line.rstrip()) for line in lines]


def find_antenas(data):
    antenas = defaultdict(list)
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char != ".":
                antenas[char].append((x, y))
    return antenas


def get_antidote_position(ant1, ant2):
    x_dist = abs(ant1[0] - ant2[0])
    y_dist = abs(ant1[1] - ant2[1])
    # print(f"Compare {ant1} and {ant2}")
    for ops in ((add, add), (sub, sub), (sub, add), (add, sub)):
        new_x = ops[0](ant1[0], x_dist)
        new_y = ops[1](ant1[1], y_dist)
        # print(f"Check ({new_x}, {new_y})")
        if new_x < 0 or new_y < 0:
            continue
        if abs(new_x - ant2[0]) == x_dist * 2 and abs(new_y - ant2[1]) == y_dist * 2:
            return new_x, new_y


def part1(data):
    antenas = find_antenas(data)
    antidote_positions = set()
    for antena_positions in antenas.values():
        for antena_position in antena_positions:
            for other_position in antena_positions:
                if antena_position == other_position:
                    continue
                new_position = get_antidote_position(antena_position, other_position)
                if (
                    new_position is not None
                    and new_position[0] < len(data[0])
                    and new_position[1] < len(data)
                ):
                    antidote_positions.add(new_position)
    #                 data[new_position[1]][new_position[0]] = "#"
    # with open(Path(Path(__file__).parent, "8_test.txt"), "w") as f:
    #     f.writelines("".join(line) + "\n" for line in data)
    print(len(antidote_positions))


def get_antidote_positions(ant1, ant2, x_len, y_len):
    x_dist = abs(ant1[0] - ant2[0])
    y_dist = abs(ant1[1] - ant2[1])
    # print(f"Compare {ant1} and {ant2}")
    for ops in ((add, add), (sub, sub), (sub, add), (add, sub)):
        new_x = ops[0](ant1[0], x_dist)
        new_y = ops[1](ant1[1], y_dist)
        # print(f"Check ({new_x}, {new_y})")
        if (abs(new_x - ant2[0]) >= x_dist and abs(new_y - ant2[1]) >= y_dist) or (
            new_x,
            new_y,
        ) == ant2:
            while new_x < x_len and new_y < y_len and new_x >= 0 and new_y >= 0:
                yield new_x, new_y
                new_x = ops[0](new_x, x_dist)
                new_y = ops[1](new_y, y_dist)


def part2(data):
    x_len = len(data[0])
    y_len = len(data)
    antenas = find_antenas(data)
    antidote_positions = set()
    for antena_positions in antenas.values():
        for antena_position in antena_positions:
            for other_position in antena_positions:
                if antena_position == other_position:
                    continue
                new_positions = get_antidote_positions(
                    antena_position, other_position, x_len, y_len
                )
                if new_positions is not None:
                    for antidote_position in new_positions:
                        antidote_positions.add(antidote_position)
    #                     data[antidote_position[1]][antidote_position[0]] = "#"
    # with open(Path(Path(__file__).parent, "8_test.txt"), "w") as f:
    #     f.writelines("".join(line) + "\n" for line in data)
    print(len(antidote_positions))


if __name__ == "__main__":
    data = read_file()
    part1(data)
    part2(data)
