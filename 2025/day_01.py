import operator
from pathlib import Path
from typing import Literal


def read_file():
    with open(Path(__file__.replace(".py", ".txt"))) as f:
        data = f.readlines()
    return [(line[0], int(line[1:].rstrip("\n"))) for line in data]


class Dial:
    MIN_VALUE = 0
    MAX_VALUE = 99
    UNIQUE_VALUES = MAX_VALUE + 1
    START_VALUE = 50

    def __init__(self, start_value: int = START_VALUE):
        self.current_value: int = start_value
        self.rotates: int = 0

    def rotate(self, direction: Literal["L", "R"], value: int):
        if direction not in ("L", "R"):
            raise ValueError(
                f"Unknown direction `{direction}`. Valid direction is `L` or `R`."
            )
        direction_op = operator.add if direction == "R" else operator.sub
        new_current_value = direction_op(self.current_value, value)

        rotates = abs(new_current_value) // self.UNIQUE_VALUES
        # +1 if negative number but don't add if started at 0
        if self.current_value != 0 and new_current_value < 1:
            rotates += 1

        new_current_value = new_current_value % self.UNIQUE_VALUES

        if new_current_value < self.MIN_VALUE or new_current_value > self.MAX_VALUE:
            raise ValueError(f"Invalid dial value: {new_current_value}")

        self.rotates += rotates
        self.current_value = new_current_value


if __name__ == "__main__":
    data = read_file()
    dial = Dial()
    final_pass = 0
    for direction, value in data:
        dial.rotate(direction, value)
        if dial.current_value == 0:
            final_pass += 1
    print(f"Part 1 = {final_pass}")
    print(f"Part 2 = {dial.rotates}")
