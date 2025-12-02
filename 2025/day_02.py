from pathlib import Path


def read_file():
    with open(Path(__file__.replace(".py", ".txt"))) as f:
        data = f.readlines()[0].split(",")
    return [rng.split("-") for rng in data]


def part_1(data):
    repeated_n = []
    for start_n, end_n in data:
        for num in range(int(start_n), int(end_n) + 1):
            num = str(num)
            if len(num) % 2 == 0:
                half_len = len(num) // 2
                num_1 = num[half_len:]
                num_2 = num[:half_len]
                if num_1 == num_2:
                    repeated_n.append(int(num))
    print(f"Part 1 = {sum(repeated_n)}")


def part_2(data):
    def _split_number(num_str: str, parts: int) -> bool:
        num_parts = [num_str[i : i + parts] for i in range(0, len(num_str), parts)]
        return len(set(num_parts)) == 1

    repeated_n = []
    for start_n, end_n in data:
        for num in range(int(start_n), int(end_n) + 1):
            num_str = str(num)
            for iter_n in range(1, len(num_str) + 1):
                # skip if can't be split into equal parts - min 2 parts
                if len(num_str) % iter_n != 0 or iter_n == len(num_str):
                    continue
                is_repeating = _split_number(num_str, iter_n)
                if is_repeating:
                    repeated_n.append(num)
                    break
    print(f"Part 2 = {sum(repeated_n)}")


if __name__ == "__main__":
    data = read_file()
    part_1(data)
    part_2(data)
