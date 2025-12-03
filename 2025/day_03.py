from pathlib import Path

data = Path(__file__.replace(".py", ".txt")).read_text()


def part1(data):
    batteries = []
    for bank in data:
        print(f"{bank = } ")
        largest1 = 0
        largest2 = 0
        num = 9
        while not largest1 or not largest2:
            # skip repeating
            # if num == int(largest1):
            #     num -= 1
            #     continue
            try:
                idx = bank.index(str(num))
                if idx + 1 == len(bank) and not largest1:
                    num -= 1
                    continue
                battery = bank[idx]
                bank = bank[idx + 1 :]
                print(f"updated bank = {bank}")
            except ValueError:
                num -= 1
                continue
            if not largest1:
                largest1 = battery
            else:
                largest2 = battery
            # reset if found 1st
            num -= 1
            if largest1 or num < 1:
                num = 9
        batteries.append(int(largest1 + largest2))
    print(f"Part1 = {sum(batteries)}")


if __name__ == "__main__":
    data = data.split("\n")
    print(data)
    part1(data)
