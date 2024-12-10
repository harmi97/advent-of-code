from pathlib import Path


def read_file():
    with open(Path(__file__.replace(".py", ".txt"))) as f:
        lines = f.readlines()
    return [[int(char) for char in line.rstrip()] for line in lines]


def get_trail_start_positions(data):
    start_positions = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == 0:
                start_positions.append((x, y))
    return start_positions


def find_paths(data, x, y):
    result = set()
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        x1 = x + dx
        y1 = y + dy
        if -1 < x1 < len(data[y]) and -1 < y1 < len(data):
            if data[y1][x1] == 9 and data[y][x] == 8:
                result.add((x1, y1))
            elif data[y1][x1] == data[y][x] + 1:
                result.update(find_paths(data, x1, y1))
    return result


def part1(data):
    start_positions = get_trail_start_positions(data)
    result = 0
    for x, y in start_positions:
        result += len(find_paths(data, x, y))
    print(result)


if __name__ == "__main__":
    data = read_file()
    part1(data)
