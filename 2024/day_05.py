from pathlib import Path


def read_file():
    ordering_rules = []
    updates = []
    with open(Path(Path(__file__).parent, "5.txt")) as f:
        lines = f.readlines()
        rules = True
        for line in lines:
            line = line.rstrip()
            if line == "":
                rules = False
                continue
            if rules:
                line = line.split("|")
                ordering_rules.append((int(line[0]), int(line[1])))
            else:
                updates.append([int(x) for x in line.split(",")])
    return ordering_rules, updates


def part1(ordering_rules, updates):
    valid_updates = []
    for update in updates:
        is_valid = True
        for i, page in enumerate(update):
            must_be_before = get_page_rules(page, ordering_rules)
            for x in must_be_before:
                if x in update[:i]:
                    is_valid = False
                    break
        if is_valid:
            valid_updates.append(update)
    result = sum(vu[len(vu) // 2] for vu in valid_updates)
    print(f"Part 1: result = {result}")


def get_page_rules(page, ordering_rules):
    must_be_before = []
    for rule_x, rule_y in ordering_rules:
        if rule_x == page:
            must_be_before.append(rule_y)
    return must_be_before


if __name__ == "__main__":
    ordering_rules, updates = read_file()
    part1(ordering_rules, updates)
