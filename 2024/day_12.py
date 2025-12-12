"""Advent of Code solution of Year 2024 Day 12."""

from collections import defaultdict
from pathlib import Path


def read_file():
    with open(Path(__file__.replace(".py", ".txt"))) as f:
        data = f.readlines()
    return [line.rstrip("\n") for line in data]


DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))
DATA = read_file()
DATA_W = len(DATA[0])
DATA_H = len(DATA)
CHECKED = []
REGIONS = defaultdict(dict)


def solve():
    result = 0
    for y, line in enumerate(DATA):
        for x, char in enumerate(line):
            region = (x, y)
            REGIONS[region]["fences"] = []
            REGIONS[region]["fields"] = []
            check_neighbors(x, y, char, region)
    # Part 1
    for region, values in REGIONS.items():
        result += len(values["fences"]) * len(values["fields"])
    print(result)
    result = 0
    # Part 2
    for region, values in REGIONS.items():
        fences = 0
        for x, y in values["fields"]:
            corners = check_corner(x, y, region)
            fences += corners
        result += fences * len(values["fields"])
    print(result)


def check_corner(x, y, region):
    corners_count = 0
    up = (x, y - 1)
    down = (x, y + 1)
    left = (x - 1, y)
    right = (x + 1, y)
    up_right = (x + 1, y - 1)
    up_left = (x - 1, y - 1)
    down_right = (x + 1, y + 1)
    down_left = (x - 1, y + 1)
    fields = REGIONS[region]["fields"]
    # !up && !left
    if up not in fields and left not in fields:
        corners_count += 1
    # !down && !left
    if down not in fields and left not in fields:
        corners_count += 1
    # !up && !right
    if up not in fields and right not in fields:
        corners_count += 1
    # !down && !right
    if down not in fields and right not in fields:
        corners_count += 1
    # up && left && !upleft
    if up in fields and left in fields and up_left not in fields:
        corners_count += 1
    # down && left && !downleft
    if down in fields and left in fields and down_left not in fields:
        corners_count += 1
    # up && right && !upright
    if up in fields and right in fields and up_right not in fields:
        corners_count += 1
    # down && right && !downright
    if down in fields and right in fields and down_right not in fields:
        corners_count += 1
    return corners_count


def check_neighbors(x, y, char, region):
    if (x, y) in CHECKED:
        return
    CHECKED.append((x, y))
    REGIONS[region]["fields"].append((x, y))
    # fences = 0
    for dx, dy in DIRECTIONS:
        x1 = x + dx
        y1 = y + dy
        # out of bounds check
        if DATA_W <= x1 or x1 < 0 and dx != 0:
            REGIONS[region]["fences"].append((x1, y1))
        elif DATA_H <= y1 or y1 < 0 and dy != 0:
            REGIONS[region]["fences"].append((x1, y1))
        elif DATA[y1][x1] != char:
            REGIONS[region]["fences"].append((x1, y1))
        elif DATA[y1][x1] == char:
            check_neighbors(x1, y1, char, region)


if __name__ == "__main__":
    data = read_file()
    solve()
