from pathlib import Path

DATA = Path(__file__.replace(".py", ".txt")).read_text()


def part1(ranges: list[tuple[int, int]], items: list[int]):
    fresh_items = 0
    for item in items:
        valid_range = [item for r in ranges if r[0] <= item <= r[1]]
        fresh_items += 1 if valid_range else 0

    print(f"Part 1  = {fresh_items}")


if __name__ == "__main__":
    data = DATA.split("\n\n")
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in data[0].split("\n")]
    items = [int(i) for i in data[1].split("\n")]

    part1(ranges, items)
