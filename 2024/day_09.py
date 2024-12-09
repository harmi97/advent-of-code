from itertools import batched
from pathlib import Path


def read_file():
    with open(Path(__file__.replace(".py", ".txt"))) as f:
        return f.read().replace("\n", "")


def transform_input(data):
    transformed_input = []
    data = data + "0" if len(data) % 2 != 0 else data
    for i, (page_len, free_space) in enumerate(batched(data, 2)):
        # transformed_input += f"{list[i]*int(page_len)}{['.']*int(free_space)}"
        transformed_input.extend([i] * int(page_len))
        transformed_input.extend(["."] * int(free_space))

    return transformed_input


def part1(transformed_input):
    transformed_input = list(transformed_input)
    reversed_input = list(char for char in reversed(transformed_input) if char != ".")
    # print(reversed_input)
    # print(transformed_input)
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
    # print(new_input)
    result = 0
    for i, char in enumerate(new_input):
        result += i * int(char)
    print(result)


if __name__ == "__main__":
    data = read_file()
    data = transform_input(data)
    part1(data)
