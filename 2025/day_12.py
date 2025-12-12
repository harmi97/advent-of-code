"""Advent of Code solution of Year 2025 Day 12.
NOTE: This is last day - there is no part2.
"""

from __future__ import annotations

from copy import deepcopy
from itertools import zip_longest
from pathlib import Path
from typing import Literal

DATA = Path(__file__.replace(".py", ".txt")).read_text(encoding="utf-8")


class Region:
    def __init__(self, width: int, length: int, presents: tuple[int]):
        self.grid = [["." for _ in range(width)] for _ in range(length)]
        self.presents = presents
        self.width = width  # x
        self.length = length  # y
        self._last_shape_position = (0, 0)

    @property
    def empty_space(self) -> int:
        """Count of empty spaces."""
        return sum(1 for y in self.grid for x in y if x == ".")

    def print(self) -> None:
        for y in self.grid:
            print(y)

    def place_shape(self, shape: Shape) -> bool:
        if shape.size > self.empty_space:
            raise ValueError(
                f"Shape takes {shape.size} places but there is only {self.empty_space} free."
            )
        small_grid = self._get_reduced_grid(shape.dimensions[1], shape.dimensions[0])
        # if len(small_grid) != shape.dimensions[1]:
        #     small_grid = [
        #         grid_y[start_x : start_x + shape.dimensions[1]]
        #         for grid_y in self.grid[start_y : start_y + shape.dimensions[0]]
        #     ]
        tmp_grid = deepcopy(self.grid)  # Make copy of a grid and replace if placable
        can_place = []
        start_x, start_y = self._last_shape_position
        for y, (grid_y, shape_y) in enumerate(zip_longest(small_grid, shape.shape)):
            if grid_y is None:
                can_place.append(False)
                break
            for x, (grid_x, shape_x) in enumerate(zip_longest(grid_y, shape_y)):
                tmp_grid_y = start_y + y
                tmp_grid_x = start_x + x
                if grid_x == "." and shape_x == ".":
                    can_place.append(True)
                elif grid_x == "." and shape_x == "#":
                    can_place.append(True)
                    tmp_grid[tmp_grid_y][tmp_grid_x] = shape_x
                else:
                    can_place.append(False)
        if all(can_place):
            self.grid = tmp_grid
            # Move col by col and only change row if last col
            return True
        self._update_position(shape.dimensions[1], shape.dimensions[0])
        return False

    def _get_reduced_grid(self, x_size: int, y_size: int) -> list[list[str]]:
        start_x, start_y = self._last_shape_position
        small_grid = [
            grid_y[start_x : start_x + x_size]
            for grid_y in self.grid[start_y : start_y + y_size]
        ]
        return small_grid

    def _update_position(self, x_size: int, y_size: int):
        start_x, start_y = self._last_shape_position
        new_start_x = start_x + x_size if start_x + x_size <= self.width else 0
        new_start_y = 0 if start_x + x_size <= self.width else start_y + y_size
        self._last_shape_position = (new_start_x, new_start_y)

    def _update_row_position(self, x_size: int, y_size: int):
        # Move row by row
        start_x, start_y = self._last_shape_position
        new_start_x = start_x + x_size if start_x + x_size <= self.width else 0
        new_start_y = 0 if start_x + x_size <= self.width else start_x + x_size
        self._last_shape_position = (new_start_x, new_start_y)


class Shape:
    def __init__(self, shape: tuple[str]):
        self.shape = shape
        self._rotation = 0
        self._size = None

    @property
    def dimensions(self) -> tuple[int, int]:
        """Width and length of object. Does not consider empty spaces."""
        return len(self.shape[0]), len(self.shape)

    @property
    def size(self) -> int:
        """Actual occupied size. Empty spaces are not counted."""
        if not self._size:
            self._size = sum(1 for y in self.shape for x in y if x == "#")
        return self._size

    def print(self) -> None:
        for y in self.shape:
            print(y)

    def rotate(self, degree: Literal[0, 90, 180, 270, 360] = 90) -> None:
        if degree not in (0, 90, 180, 270, 360):
            raise ValueError(
                f"Invalid degree value `{degree}` only 90 degree rotations allowed!"
            )
        if degree in (0, 360):
            return
        self._rotation = degree
        for _ in range(degree // 90):
            self.shape = list(zip(*self.shape[::-1]))

    def reset_rotation(self) -> None:
        if self._rotation == 0:
            return
        self.rotate(360 - self._rotation)


def part1(shapes: tuple[Shape], regions: tuple[Region]):
    filled_regions = 0
    for region in regions:
        # print("START")
        # region.print()
        # print()
        shape_placed = []
        for shape_idx, shape_count in enumerate(region.presents):
            shape = shapes[shape_idx]
            placements = 0
            for _ in range(shape_count):
                # Rotate till placed
                rotations = 0
                placed = False
                while not placed and rotations <= 3:
                    placed = region.place_shape(shape)
                    if not placed:
                        shape.rotate()
                        rotations += 1
                    else:
                        placements += 1
                        shape.reset_rotation()
                        break
            region.print()
            shape_placed.append(placements)
            # break  # TODO: Remove
        if region.presents == tuple(shape_placed):
            filled_regions += 1
        break  # TODO: Remove - stop at first region
    print(f"Part 1 = {filled_regions}")


def part1_simple(shapes: tuple[Shape], regions: tuple[Region]):
    """Simple solution that only counts available space. Does not actually places anything."""
    filled_regions = 0
    for region in regions:
        region_size = region.width * region.length
        for shape_idx, shape_count in enumerate(region.presents):
            shape = shapes[shape_idx]
            shape_size = shape.size * shape_count
            region_size -= shape_size
        if region_size >= 0:
            filled_regions += 1
    print(f"Part 1 = {filled_regions}")


if __name__ == "__main__":
    data = DATA.split("\n\n")
    shapes = tuple(Shape(tuple(s.splitlines()[1:])) for s in data[:-1])
    regions = (
        Region(
            width=int(r.split(":")[0].split("x")[0]),
            length=int(r.split(":")[0].split("x")[1]),
            presents=tuple(int(p) for p in r.split(":")[-1].strip().split(" ")),
        )
        for r in data[-1].splitlines()
    )
    part1_simple(shapes, regions)
