import re
from pathlib import Path


def read_file():
    with open(Path(Path(__file__).parent, "3.txt")) as f:
        data = f.readlines()
    return "".join(x.rstrip() for x in data)


def part1(data):
    data = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", data)
    mul_sum = 0
    for d in data:
        d = re.findall(r"[0-9]{1,3}", d)
        mul_sum += int(d[0]) * int(d[1])
    print(f"Part 1: result = {mul_sum}")


def part2(data):
    do_parts = re.sub(
        r"(don't\(\).*?do\(\)|don't\(\).*?$)",
        "",
        data,
    )
    mul_sum = 0
    mul_parts = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", do_parts)
    for mul_part in mul_parts:
        mul_part = re.findall(r"[0-9]{1,3}", mul_part)
        mul_sum += int(mul_part[0]) * int(mul_part[1])
    print(f"Part 2: result = {mul_sum}")


if __name__ == "__main__":
    reports = read_file()
    part1(reports)
    part2(reports)
