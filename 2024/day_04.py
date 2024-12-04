from pathlib import Path

XMAS = "XMAS"

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


def read_file():
    with open(Path(Path(__file__).parent, "4.txt")) as f:
        data = f.readlines()
    return data


def check(x, y, data):
    n_xmas = 0
    for direction, coords in DIRECTIONS.items():
        # print(f"Checking ({x}, {y}) {direction=}")
        x_range = (
            range(0, 4 * coords[0], 1 * coords[0]) if coords[0] != 0 else (0, 0, 0, 0)
        )
        y_range = (
            range(0, 4 * coords[1], 1 * coords[1]) if coords[1] != 0 else (0, 0, 0, 0)
        )
        chars = ""
        for idx, (x_diff, y_diff) in enumerate(zip(x_range, y_range)):
            try:
                x_coord = x + x_diff
                y_coord = y + y_diff
                if (
                    x_coord >= 0
                    and y_coord >= 0
                    and data[y_coord][x_coord] == XMAS[idx]
                ):
                    # print(f"({x_coord},{y_coord}) {data[x_coord][y_coord]}")
                    chars += data[y_coord][x_coord]
                    continue
                break
            except IndexError:
                break
        if chars == XMAS:
            # print(f"---- Found XMAS ({x}, {y}) {direction=}")
            n_xmas += 1
    return n_xmas


def part1(data):
    n_xmas = 0
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == "X":
                result = check(x, y, data)
                n_xmas += result
    return n_xmas


def part2(data):
    pass


if __name__ == "__main__":
    data = read_file()
    print(f"Part 1: result = {part1(data)}")
    print(f"Part 2: result = {part2(data)}")
