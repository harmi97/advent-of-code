"""Advent of Code solution of Year 2024 Day 2."""

from pathlib import Path


def read_file():
    reports = []
    with open(Path(Path(__file__).parent, "2.txt")) as f:
        lines = f.readlines()
        for line in lines:
            report_line = line.split(" ")
            reports.append([int(x) for x in report_line])
    return reports


def report_checker(report: list):
    prev_level = None
    is_asc = False
    is_desc = False
    incorrect_idx = []
    for i, level in enumerate(report):
        if prev_level is None:
            prev_level = level
            continue
        diff = prev_level - level
        if not (abs(diff) >= 1 and abs(diff) <= 3):
            incorrect_idx.append(i)
        if diff < 0:
            is_asc = True
        else:
            is_desc = True
        if is_asc and is_desc:
            incorrect_idx.append(i)
        prev_level = level
    return incorrect_idx


def part1(reports):
    safe_count = 0
    for report in reports:
        result = report_checker(report)
        if not result:
            safe_count += 1
    print(f"Part 1: result = {safe_count}")


def part2(reports):
    safe_count = 0
    for report in reports:
        incorrect_idx = report_checker(report)
        if not incorrect_idx:
            safe_count += 1
        else:
            # Add fist/last index edge case
            incorrect_idx.append(1)
            incorrect_idx.append(len(report))
            for i in incorrect_idx:
                report_copy = report.copy()
                report_copy.pop(i - 1)
                incorrect_idx = report_checker(report_copy)
                if not incorrect_idx:
                    safe_count += 1
                    break
    print(f"Part 2: result = {safe_count}")


if __name__ == "__main__":
    reports = read_file()
    part1(reports)
    part2(reports)
