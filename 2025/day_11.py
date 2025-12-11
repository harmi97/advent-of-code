from collections import Counter
from functools import lru_cache
from pathlib import Path

DATA = Path(__file__.replace(".py", ".txt")).read_text(encoding="utf-8")

YOU = "you"  # part1 start
OUT = "out"  # end
SVR = "svr"  # part2 start
FFT = "fft"  # part2
DAC = "dac"  # part2


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


@lru_cache(maxsize=None)
def find_path2(
    current_output: str = None,
    fft_found=False,
    dac_found=False,
) -> list[str]:
    paths = 0
    current_output = current_output or SVR
    if current_output == OUT and fft_found and dac_found:
        paths += 1
    for next_output in data_part2.get(current_output, []):
        paths += find_path2(
            current_output=next_output,
            fft_found=fft_found or current_output == FFT,
            dac_found=dac_found or current_output == DAC,
        )
    return paths


def part1(data: dict[str, list[str]]):
    full_path = find_path(data)
    counter = Counter(full_path)
    print(f"Part 1 = {counter[OUT]}")


def part2(data: dict[str, list[str]]):
    global data_part2
    data_part2 = data
    paths_count = find_path2()
    print(f"Part 2 = {paths_count}")


if __name__ == "__main__":
    data = DATA.splitlines()
    data = {line.split(" ")[0].strip(":"): line.split(" ")[1:] for line in data}
    part1(data)
    part2(data)
