"""Advent of Code solution of Year 2025 Day 10."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path

from z3 import Int, Optimize, Sum, sat

DATA = Path(__file__.replace(".py", ".txt")).read_text(encoding="utf-8")


class Machine:
    LIGHT_ON = "#"
    LIGHT_OFF = "."

    @classmethod
    def from_line(cls, line: str) -> Machine:
        line = line.split(" ")
        machine = cls(
            lights=line[0].strip("[]"),
            joltage=tuple(int(j) for j in line[-1].strip("{}").split(",")),
            buttons=tuple(eval(b.replace(")", ",)")) for b in line[1:-1]),
        )
        return machine

    def __init__(self, lights: str, buttons: tuple[tuple[int]], joltage: tuple[int]):
        self.lights = "." * len(lights)
        self.lights_end_position = lights
        self.buttons = buttons
        self.joltage = [0] * len(joltage)
        self.joltage_end_position = joltage

    @property
    def lights_count(self) -> int:
        return len(self.lights_end_position)

    @property
    def buttons_count(self) -> int:
        return len(self.buttons)

    def reset_machine(self) -> None:
        """Resets lights and joltage to starting position."""
        self.lights = "." * len(self.lights)
        self.joltage = [0] * len(self.joltage)

    def press_button(
        self, button_idx: int | None = None, button_value: tuple[int] | None = None
    ):
        """Presses button and flips wired lights to that button.

        Args:
            button_idx (int | None, optional): Index of button in button list. Defaults to None.
            button_value (tuple[int] | None, optional): Value of a button from button list.
                Defaults to None.

        Raises:
            ValueError: Raised when called without any parameter.
            ValueError: Raised when invalid button index is passed.
            ValueError: Raised when invalid button value is passed.
        """
        if button_idx is None and button_value is None:
            raise ValueError(
                "Missing `button_idx` or `button_value` parameter value. Pick one."
            )
        if button_idx is not None and (
            button_idx >= self.buttons_count or button_idx < 0
        ):
            raise ValueError(
                f"Invalid button index `{button_idx}`. "
                f"Pick range from 0 to {self.buttons_count - 1}"
            )
        if button_value is not None and button_value not in self.buttons:
            raise ValueError(
                f"Button is not available. Available buttons `{self.buttons}`."
            )
        if button_value:
            button_idx = self.buttons.index(button_value)
        for idx in self.buttons[button_idx]:
            self._flip_light(idx)
            self.joltage[idx] += 1

    def _flip_light(self, light_idx: int):
        """Flips the light at specified index."""
        if light_idx >= self.lights_count or light_idx < 0:
            raise ValueError(
                f"Invalid light index `{light_idx}`. "
                f"Pick range from 0 to {self.lights_count - 1}"
            )
        lights = list(self.lights)
        is_on = lights[light_idx] == self.LIGHT_ON
        lights[light_idx] = self.LIGHT_OFF if is_on else self.LIGHT_ON
        self.lights = "".join(lights)


def part1(machines: list[Machine]):
    min_presses_list = []
    for machine in machines:
        min_presses = 99999
        presses_combinations = [
            combo
            for n_buttons in range(1, machine.buttons_count + 1)
            for combo in combinations(machine.buttons, n_buttons)
        ]
        for combo in presses_combinations:
            presses = 0
            machine.reset_machine()
            for button in combo:
                presses += 1
                machine.press_button(button_value=button)
                if machine.lights == machine.lights_end_position:
                    min_presses = min(min_presses, presses)
                    break
        min_presses_list.append(min_presses)
    print(f"Part 1 = {sum(min_presses_list)}")


def part2(machines: list[Machine]):
    min_presses_list = []
    for machine in machines:
        num_buttons = machine.buttons_count
        num_lights = machine.lights_count
        opt = Optimize()
        presses = [Int(f"presses_{idx}") for idx in range(num_buttons)]
        for var in presses:
            opt.add(var >= 0)
        for light_idx in range(num_lights):
            contributing_buttons = [
                presses[button_idx]
                for button_idx, button in enumerate(machine.buttons)
                if light_idx in button
            ]
            target = machine.joltage_end_position[light_idx]
            if contributing_buttons:
                opt.add(Sum(contributing_buttons) == target)
            else:
                if target != 0:
                    raise ValueError("No button affects light")
        total_presses = Sum(presses)
        opt.minimize(total_presses)
        if opt.check() != sat:
            raise ValueError("No solution")
        model = opt.model()
        min_presses = sum(model[var].as_long() for var in presses)
        min_presses_list.append(min_presses)
    print(f"Part 2 = {sum(min_presses_list)}")


if __name__ == "__main__":
    data = DATA.splitlines()
    machines = [Machine.from_line(line) for line in data]
    part1(machines)
    part2(machines)
