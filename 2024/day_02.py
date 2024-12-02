from pathlib import Path


def read_file():
    reports = []
    with open(Path(Path(__file__).parent, "2.txt")) as f:
        lines = f.readlines()
        for line in lines:
            report_line = line.split(" ")
            reports.append([int(x) for x in report_line])
    return reports


def part1(reports):
    safe_count = 0
    for report in reports:
        prev_level = None
        diffs = []
        for level in report:
            if prev_level is None:
                prev_level = level
                continue
            diff = prev_level - level
            diffs.append(diff)
            prev_level = level
        if not all(abs(diff) >= 1 and abs(diff) <= 3 for diff in diffs):
            continue
        if report == sorted(report) or report == sorted(report, reverse=True):
            print(f"{report=} is safe!")
            safe_count += 1
    print(f"Part 1: result = {safe_count}")


def part2(reports):
    pass
    # print(f"Part 2: result = {safe_count}")


if __name__ == "__main__":
    reports = read_file()
    part1(reports)
    part2(reports)
