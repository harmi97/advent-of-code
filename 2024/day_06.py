from pathlib import Path

# (x,y) axes
DIRECTIONS = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0),
}


def read_file():
    with open(Path(Path(__file__).parent, "6.txt")) as f:
        data = f.readlines()
    return [list(line) for line in data]


def get_starting_position(data):
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "^":
                return x, y


def part1(data):
    x0, y0 = get_starting_position(data)
    is_out_of_bounds = False
    direction = 0
    steps = 1
    data[y0][x0] = "X"
    while not is_out_of_bounds:
        x_diff, y_diff = DIRECTIONS[list(DIRECTIONS.keys())[direction]]
        try:
            x1 = x0 + x_diff
            y1 = y0 + y_diff
            if x1 < 0 or y1 < 0:
                raise IndexError
            next_position = data[y1][x1]
            if next_position == "#":
                direction = direction + 1 if direction < 3 else 0
            else:
                if next_position == ".":
                    data[y1][x1] = "X"
                    steps += 1
                x0 = x1
                y0 = y1
        except IndexError:
            is_out_of_bounds = True
    print(f"Part 1 result: {steps}")
    with open(Path(Path(__file__).parent, "6_new.txt"), "w") as f:
        f.writelines(["".join(row) for row in data])


if __name__ == "__main__":
    data = read_file()
    part1(data)
