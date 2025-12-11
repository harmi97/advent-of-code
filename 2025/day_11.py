from collections import Counter
from pathlib import Path

DATA = Path(__file__.replace(".py", ".txt")).read_text(encoding="utf-8")

YOU = "you"
OUT = "out"


def find_path(
    data: dict, path: list | None = None, current_output: str = None
) -> list[str]:
    path = path or []
    if current_output == OUT:
        path.append(current_output)
        return path
    current_output = current_output or YOU
    path.append(current_output)
    for next_output in data[current_output]:
        find_path(data, path, next_output)
    return path


def part1(data: dict[str, list[str]]):
    full_path = find_path(data)
    counter = Counter(full_path)
    print(f"Part 1 = {counter[OUT]}")


if __name__ == "__main__":
    data = DATA.splitlines()
    data = {line.split(" ")[0].strip(":"): line.split(" ")[1:] for line in data}
    part1(data)
