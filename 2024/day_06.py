from copy import deepcopy
from pathlib import Path

from tqdm import tqdm

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


def part1(data, print_result=False):
    x0, y0 = get_starting_position(data)
    is_out_of_bounds = False
    direction = 0
    steps = 1
    data[y0][x0] = "X"
    while not is_out_of_bounds:
        dx, dy = DIRECTIONS[list(DIRECTIONS.keys())[direction]]
        try:
            x1 = x0 + dx
            y1 = y0 + dy
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
                yield (x1, y1, dx, dy)
        except IndexError:
            is_out_of_bounds = True
    if print_result:
        print(f"Part 1 result: {steps}")


def part2(data, coords):
    loop_positions = 0
    for x, y in tqdm(coords):
        new_data = deepcopy(data)
        new_data[y][x] = "#"
        new_coords = set()
        for coord in part1(new_data):
            # Compare against position and direction if it repeats there is loop
            if coord in new_coords:
                loop_positions += 1
                break
            new_coords.add(coord)
    print(f"Part 2 result: {loop_positions}")


if __name__ == "__main__":
    data = read_file()
    part1_generator = part1(deepcopy(data), print_result=True)
    start_coords = get_starting_position(data)
    coords = set((x, y) for x, y, _, _ in part1_generator if (x, y) != start_coords)
    part2(data, coords)
