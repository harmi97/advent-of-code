from pathlib import Path

from tqdm import tqdm


def read_file():
    with open(Path(__file__.replace(".py", ".txt"))) as f:
        line = f.read()
    return [int(x) for x in line.split(" ")]


def apply_rules(value):
    if value == 0:
        value = 1
    elif len(str(value)) % 2 == 0:
        v_len = int(len(str(value)) / 2)
        value = [int(str(value)[:v_len]), int(str(value)[v_len:])]
    else:
        value = value * 2024
    return value


def solve(data, blinks):
    for _ in tqdm(range(blinks)):
        new_data = []
        for value in data:
            new_val = apply_rules(value)
            if isinstance(new_val, list):
                new_data.extend(new_val)
            else:
                new_data.append(new_val)
        data = new_data
        # print(f"Blink {x} = {data}")
    print(len(data))


if __name__ == "__main__":
    data = read_file()
    solve(data, 25)  # part 1
    solve(data, 75)  # part 2
