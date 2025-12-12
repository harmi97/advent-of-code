"""Advent of Code solution of Year 2024 Day 9."""

from itertools import batched
from pathlib import Path

from tqdm import tqdm


def read_file():
    with open(Path(__file__.replace(".py", ".txt"))) as f:
        return f.read().replace("\n", "")


def transform_input(data, part1=True):
    transformed_input = []
    data = data + "0" if len(data) % 2 != 0 else data
    for i, (page_len, free_space) in enumerate(batched(data, 2)):
        page = [i] * int(page_len)
        fspace = ["."] * int(free_space)
        if part1:
            transformed_input.extend(page)
            transformed_input.extend(fspace)
        else:
            transformed_input.append(page)
            if fspace:
                transformed_input.extend(fspace)
    return transformed_input


def part1(transformed_input):
    transformed_input = list(transformed_input)
    reversed_input = list(char for char in reversed(transformed_input) if char != ".")
    new_input = ["."] * len(reversed_input)
    pos = 0
    for i, char in enumerate(transformed_input):
        if char == ".":
            new_input[i] = reversed_input[pos]
            pos += 1
        else:
            new_input[i] = char
        if "." not in new_input:
            break
    result = 0
    for i, char in enumerate(new_input):
        result += i * int(char)
    print(result)


def part2(transformed_input):
    transformed_input = list(transformed_input)
    for page_block in tqdm(reversed(transformed_input), total=len(transformed_input)):
        if not isinstance(page_block, list):
            continue
        old_page_idx = transformed_input.index(page_block)
        empty_space = 0
        for i, char in enumerate(transformed_input):
            if char == ".":
                empty_space += 1
            elif char != "." and empty_space >= len(page_block):
                idx_shift = empty_space - len(page_block)
                for idx, page in enumerate(page_block):
                    new_page_idx = (i - 1 - idx_shift) + idx * -1
                    if new_page_idx < old_page_idx:
                        if idx == 0:
                            transformed_input[old_page_idx] = "."
                        else:
                            transformed_input.insert(old_page_idx, ".")
                        transformed_input[new_page_idx] = page
                break
            else:
                empty_space = 0
    result = 0
    new_input = []
    for x in transformed_input:
        if isinstance(x, list):
            new_input.extend(x)
        else:
            new_input.append(x)
    for i, char in enumerate(new_input):
        if char == ".":
            continue
        result += i * int(char)
    print(result)


if __name__ == "__main__":
    data = read_file()
    transformed_input = transform_input(data)
    part1(transformed_input)
    transformed_input = transform_input(data, part1=False)
    part2(transformed_input)
