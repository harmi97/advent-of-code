import re
from itertools import batched, product
from pathlib import Path

from tqdm import tqdm

OPERATORS = ("+", "*")


def read_file():
    with open(Path(Path(__file__).parent, "7.txt")) as f:
        lines = f.readlines()
    return [re.findall(r"[0-9]{1,}", line) for line in lines]


def part1(data):
    result = 0
    for row in tqdm(data):
        expected_result = int(row[0])
        values = list(batched(row[1:], n=2))
        formula = ""
        for i, pair in enumerate(values):
            if i == 0:
                formula = f"({pair[0]}" + "{}" + f"{pair[1]})"
            elif len(pair) == 2 and i != 0:
                formula = f"(({formula}" + "{}" + f"{pair[0]})" + "{}" + f"{pair[1]})"
            else:
                formula = f"({formula}" + "{}" + f"{pair[0]})"
        operators = list(product(OPERATORS, repeat=len(row[1:]) - 1))
        test_passed = False
        for ops in operators:
            formula_with_ops = formula.format(*ops)
            if expected_result == eval(formula_with_ops):
                test_passed = True
        if test_passed:
            result += expected_result
    print(result)


if __name__ == "__main__":
    data = read_file()
    part1(data)
