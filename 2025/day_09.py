from copy import deepcopy
from pathlib import Path

from shapely.geometry.polygon import Polygon
from tqdm import tqdm

DATA = Path(__file__.replace(".py", ".txt")).read_text(encoding="utf-8")


# class Polygon:
# def __init__(self, points: list[tuple[int, int]]):
#     self.points = sorted(points)

# def is_inside(self, point: tuple[int, int]) -> bool:
#     x, y = point[0], point[1]
#     n = len(self.points)
#     inside = False
#     p1x, p1y = self.points[0]
#     for i in range(n + 1):
#         p2x, p2y = self.points[i % n]
#         if y > min(p1y, p2y):
#             if y <= max(p1y, p2y):
#                 if x <= max(p1x, p2x):
#                     if p1y != p2y:
#                         xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
#                     if p1x == p2x or x <= xints:
#                         inside = not inside
#         p1x, p1y = p2x, p2y
#     print(point, inside)
#     return inside


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
    # polygon = Polygon(data)
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
    # data.sort()
    part1(data)
    part2(data)
