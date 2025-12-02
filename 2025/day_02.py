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
    print(sum(repeated_n))


if __name__ == "__main__":
    data = read_file()
    part_1(data)
