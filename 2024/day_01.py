from pathlib import Path


def read_file():
    list1 = []
    list2 = []
    with open(Path(Path(__file__).parent, "1.txt")) as f:
        lines = f.readlines()
        for line in lines:
            col1, col2 = line.split("   ")
            list1.append(int(col1))
            list2.append(int(col2))
    return list1, list2


def part1(list1, list2):
    distance = 0
    for c1, c2 in zip(sorted(list1), sorted(list2)):
        distance += abs(c1 - c2)
    print(f"Part 1: result = {distance}")


def part2(list1, list2):
    list1_count = {}.fromkeys(set(list1), 0)
    for x in list2:
        if x in list1_count.keys():
            list1_count[x] += 1
    result = sum(k * v for k, v in list1_count.items())
    print(f"Part 2: {result = }")


if __name__ == "__main__":
    list1, list2 = read_file()
    part1(list1, list2)
    part2(list1, list2)
