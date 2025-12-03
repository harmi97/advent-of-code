from pathlib import Path

data = Path(__file__.replace(".py", ".txt")).read_text()


def find_largest(data: list[str], max_batteries: int) -> list[int]:
    battery_banks = []
    for battery_bank in data:
        battery_bank = [int(x) for x in battery_bank]
        batteries = []
        start_i = 0  # Starting position of search
        while len(batteries) != max_batteries:
            # Edge-case when 1st value is max
            if start_i == 0 and batteries:
                battery_bank[start_i] = 0
            # Add + 1 to include previous max number found
            start_i = start_i if not batteries else start_i + 1
            if start_i != 0:
                battery_bank[:start_i] = [0] * start_i
            end_i = len(battery_bank) - (max_batteries - len(batteries)) + 1
            # Search only in limited window
            search_area = battery_bank[start_i:end_i]
            if not search_area:
                break
            max_battery = max(search_area)
            start_i = battery_bank.index(max_battery)
            batteries.append(max_battery)
        battery_banks.append(int("".join([str(b) for b in batteries])))
    return battery_banks


def part1(data):
    battery_banks = find_largest(data, max_batteries=2)
    print(f"Part1 = {sum(battery_banks)}")


def part2(data):
    battery_banks = find_largest(data, max_batteries=12)
    print(f"Part2 = {sum(battery_banks)}")


if __name__ == "__main__":
    data = data.split("\n")
    part1(data=data)
    part2(data=data)
