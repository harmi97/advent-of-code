from copy import deepcopy
from pathlib import Path

from tqdm import tqdm

DATA = Path(__file__.replace(".py", ".txt")).read_text(encoding="utf-8")


def part1(data: list[tuple(int, int)]):
    print("Running Part 1")
    max_area = 0
    for tile in tqdm(data):
        other_tiles = deepcopy(data)
        for other_tile in other_tiles:
            area = abs((tile[0] + 1 - other_tile[0]) * (tile[1] + 1 - other_tile[1]))
            max_area = max(max_area, area)
    print(f"Part 1  = {max_area}")


if __name__ == "__main__":
    data = DATA.splitlines()
    data = [tuple(int(x) for x in r.split(",")) for r in data]
    data.sort()
    part1(data)
