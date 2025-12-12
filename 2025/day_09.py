"""Advent of Code solution of Year 2025 Day 9."""

from copy import deepcopy
from pathlib import Path

from shapely.geometry.polygon import Polygon
from tqdm import tqdm

DATA = Path(__file__.replace(".py", ".txt")).read_text(encoding="utf-8")


def part1(data: list[tuple[int, int]]):
    print("Running Part 1")
    max_area = 0
    for tile in tqdm(data):
        other_tiles = deepcopy(data)
        for other_tile in other_tiles:
            corners = [
                tile,
                other_tile,
                (tile[0], other_tile[1]),
                (other_tile[0], tile[1]),
            ]
            corners.sort()
            area = (corners[1][1] - corners[0][1] + 1) * (
                corners[2][0] - corners[0][0] + 1
            )
            max_area = max(max_area, area)
    print(f"Part 1  = {max_area}")


def part2(data: list[tuple[int, int]]):
    print("Running Part 2")
    polygon = Polygon(data)
    max_area = 0
    for tile in tqdm(data):
        other_tiles = deepcopy(data)
        other_tiles.remove(tile)
        for other_tile in other_tiles:
            corners = [
                tile,
                other_tile,
                (tile[0], other_tile[1]),
                (other_tile[0], tile[1]),
            ]
            corners.sort()
            is_inside = False
            area = (corners[1][1] - corners[0][1] + 1) * (
                corners[2][0] - corners[0][0] + 1
            )
            if area > max_area:
                polygon2 = Polygon.from_bounds(
                    corners[0][0], corners[0][1], corners[1][0], corners[1][1]
                )
                xs = [c[0] for c in corners]
                ys = [c[1] for c in corners]
                polygon2 = Polygon.from_bounds(min(xs), min(ys), max(xs), max(ys))
                is_inside = polygon.covers(polygon2)
                if is_inside:
                    max_area = max(max_area, area)
    print(f"Part 2  = {max_area}")


if __name__ == "__main__":
    data = DATA.splitlines()
    data = [tuple(int(x) for x in r.split(",")) for r in data]
    part1(data)
    part2(data)
