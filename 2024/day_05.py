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


def get_page_rules(page, ordering_rules):
    must_be_before = []
    for rule_x, rule_y in ordering_rules:
        if rule_x == page:
            must_be_before.append(rule_y)
    return must_be_before


def part1(ordering_rules, updates):
    valid_updates = []
    for update in updates:
        invalid_page_idx = validate_update(update, ordering_rules)
        if not invalid_page_idx:
            valid_updates.append(update)
    result = sum(vu[len(vu) // 2] for vu in valid_updates)
    print(f"Part 1: result = {result}")


def validate_update(update, ordering_rules):
    for i, page in enumerate(update):
        must_be_before = get_page_rules(page, ordering_rules)
        for x in must_be_before:
            if x in update[:i]:
                # print(f"{page} {must_be_before = }")
                return i


# thanks to u/causticmango
def reorder_update(update: list, ordering_rules, invalid_page_idx):
    while validate_update(update, ordering_rules):
        for x1, x2 in ordering_rules:
            if x1 in update and x2 in update:
                i1 = update.index(x1)
                i2 = update.index(x2)
                if i1 > i2:
                    update[i1], update[i2] = update[i2], update[i1]
    return update


def part2(ordering_rules, updates):
    valid_updates = []
    for update in updates:
        invalid_page_idx = validate_update(update, ordering_rules)
        if not invalid_page_idx:
            continue
        print(f"{update = } is not valid reordering")
        update = reorder_update(update, ordering_rules, invalid_page_idx)
        invalid_page_idx = validate_update(update, ordering_rules)
        if invalid_page_idx:
            print(f"{update = } reordering failed")
        else:
            valid_updates.append(update)
    result = sum(vu[len(vu) // 2] for vu in valid_updates)
    print(f"Part 2: result = {result}")


if __name__ == "__main__":
    xx = []
    ordering_rules, updates = read_file()
    part1(ordering_rules, updates)
    part2(ordering_rules, updates)
