from pathlib import Path

from tqdm import tqdm


def read_file():
    with open(Path(__file__.replace(".py", ".txt"))) as f:
        line = f.read()
    return [int(x) for x in line.split(" ")]


RESULTS_MAP = {}


def apply_rules_rec(value, iter, max_iter):
    if iter >= max_iter:
        return 0
    result = RESULTS_MAP.get((value, iter), 0)
    if result:
        return result
    if value == 0:
        result += apply_rules_rec(1, iter + 1, max_iter)
    elif len(str(value)) % 2 == 0:
        result += 1
        v_len = int(len(str(value)) / 2)
        result += apply_rules_rec(int(str(value)[:v_len]), iter + 1, max_iter)
        result += apply_rules_rec(int(str(value)[v_len:]), iter + 1, max_iter)
    else:
        result += apply_rules_rec(value * 2024, iter + 1, max_iter)
    RESULTS_MAP[(value, iter)] = result
    return result


def solve2(data, blinks):
    result = 0
    for value in tqdm(data):
        result += 1
        result += apply_rules_rec(value, 0, blinks)
    return result


if __name__ == "__main__":
    data = read_file()
    print(f"Part 1 result = {solve2(data, 25)}")
    RESULTS_MAP = {}
    print(f"Part 2 result = {solve2(data, 75)}")
