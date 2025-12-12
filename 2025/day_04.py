"""Advent of Code solution of Year 2025 Day 4."""

from pathlib import Path

DATA = Path(__file__.replace(".py", ".txt")).read_text()
ROLL = "@"
# (x,y) axes
DIRECTIONS = {
    "horizontal_right": (1, 0),
    "horizontal_left": (-1, 0),
    "vertical_up": (0, -1),
    "vertical_down": (0, 1),
    "diagonal_up_right": (1, -1),
    "diagonal_up_left": (-1, -1),
    "diagonal_down_right": (1, 1),
    "diagonal_down_left": (-1, 1),
}
MAX_ROLLS = 4


def is_valid_position(col_x: int, row_y: int, data: list[list[str]]):
    min_row_idx = 0
    min_col_idx = 0
    max_row_idx = len(data) - 1
    max_col_idx = len(data[0]) - 1
    rolls_in_reach = 0
    for x_diff, y_diff in DIRECTIONS.values():
        # Get position to check
        new_y = row_y + y_diff
        new_x = col_x + x_diff
        # Out of bounds positions
        if (
            new_y < min_row_idx
            or new_x < min_col_idx
            or new_y > max_row_idx
            or new_x > max_col_idx
        ):
            continue
        if data[new_y][new_x] == ROLL:
            rolls_in_reach += 1
        if rolls_in_reach >= MAX_ROLLS:
            return False
    return True


def part1(data: list[list[str]]):
    valid_positions = []
    for row_y, row in enumerate(data):
        # print()
        for col_x, col in enumerate(row):
            if col != ROLL:
                # print(".", end="")
                continue
            if is_valid_position(col_x, row_y, data):
                # print("x", end="")
                valid_positions.append((col_x, row_y))
                continue
            # print(col, end="")
    print(f"Part 1 = {len(valid_positions)}")


def part2(data: list[list[str]]):
    rolls_removed = []
    while True:
        rolls_removed_iter = []
        for row_y, row in enumerate(data):
            for col_x, col in enumerate(row):
                if col != ROLL:
                    continue
                if is_valid_position(col_x, row_y, data):
                    data[row_y][col_x] = "."
                    rolls_removed_iter.append((col_x, row_y))
                    continue
        # Stop if no more rolls could be removed
        if not rolls_removed_iter:
            break
        rolls_removed.extend(rolls_removed_iter)
    print(f"Part 2 = {len(rolls_removed)}")


if __name__ == "__main__":
    data = DATA.split("\n")
    data = [list(row) for row in data]
    part1(data)
    part2(data)
