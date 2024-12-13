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


def part1():
    result = 0
    for y, line in enumerate(DATA):
        for x, char in enumerate(line):
            region = (x, y)
            REGIONS[region]["fences"] = []
            REGIONS[region]["fields"] = 0
            check_neighbors(x, y, char, region)
    for region in REGIONS.values():
        result += len(region["fences"]) * region["fields"]
    print(result)


def check_neighbors(x, y, char, region):
    if (x, y) in CHECKED:
        return
    CHECKED.append((x, y))
    REGIONS[region]["fields"] += 1
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
    part1()

# 1402544
# 871983
