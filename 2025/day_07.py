from pathlib import Path

DATA = Path(__file__.replace(".py", ".txt")).read_text()
SPLITTER = "^"
START = "S"


def part1(data: list[list[str]]):
    splitter_hits = 0
    beam_indexes = {data[0].index(START)}
    for line in data:
        if set(line) == {"."}:
            continue
        while True:
            try:
                splitter_idx = line.index(SPLITTER)
            except ValueError:
                break
            line[splitter_idx] = "X"
            # do not count if beam is not above
            if splitter_idx not in beam_indexes:
                continue
            splitter_hits += 1
            beam_indexes.remove(splitter_idx)
            beam_indexes.add(splitter_idx + 1)  # right
            beam_indexes.add(splitter_idx - 1)  # left
    print(f"Part 1  = {splitter_hits}")


if __name__ == "__main__":
    data = DATA.splitlines()
    data = [list(r) for r in data]
    part1(data)
