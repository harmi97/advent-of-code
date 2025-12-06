import math
from pathlib import Path

DATA = Path(__file__.replace(".py", ".txt")).read_text()


def part1(data: list[list[str]]):
    results = []
    max_cols = len(data[0])
    max_rows = len(data) - 1
    for idx_c in range(max_cols):
        numbers = [int(data[idx_r][idx_c]) for idx_r in range(max_rows)]
        op = data[-1][idx_c]
        if op == "+":
            results.append(sum(numbers))
        if op == "*":
            results.append(math.prod(numbers))

    print(f"Part 1  = {sum(results)}")


if __name__ == "__main__":
    data = DATA.splitlines()
    data = [[r1 for r1 in r0.strip(" ").split((" ")) if r1 != ""] for r0 in data]
    part1(data)
