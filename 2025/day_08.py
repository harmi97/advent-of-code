import math
from copy import deepcopy
from pathlib import Path

from tqdm import tqdm

DATA = Path(__file__.replace(".py", ".txt")).read_text(encoding="utf-8")
MAX_CONNECTIONS = 1000


def calculate_distances(input_data: list[tuple[int, int, int]]) -> dict[float, tuple]:
    """Calculates distance between each junction box.

    Args:
        input_data (list[tuple[int, int, int]]):
            List of tuples with X, Y Z coordinates of junction boxes.
    Raises:
        ValueError: Raised when identical distance is calculated.
    Returns:
        dict[float, tuple]: Sorted dictionary with distance as key and tuple with junction box pair.
    """
    print("Calculating distances")
    distances = {}
    for jbox in tqdm(input_data):
        other_jboxes = deepcopy(input_data)
        other_jboxes.remove(jbox)
        for other_jbox in other_jboxes:
            distance = math.dist(jbox, other_jbox)
            if distance in distances.keys() and distances[distance] != (
                other_jbox,
                jbox,
            ):
                raise ValueError
            distances[distance] = (jbox, other_jbox)
    return dict(sorted(distances.items()))


def make_circuits(
    input_data: list[tuple[int, int, int]],
    distances: dict[float, tuple],
    max_connections: int | None = None,
) -> list:
    """Connects closest junction boxes with each other creating circuits.

    Args:
        input_data (list[tuple[int, int, int]]):
            List of tuples with X, Y Z coordinates of junction boxes.
        distances (dict[float, tuple]):
            Sorted dictionary with distance as key and tuple with junction box pair.
        max_connections (int | None, optional): Maximum allowed connections that can be made.
            If set to None all junction boxes are connected into single circuit.
            Defaults to None.
    Returns:
        list: List of new circuits with connected junction boxes.
    """
    print("Making connections")
    remaining_jboxes = deepcopy(input_data)
    new_circuits = []
    connections = 0
    for jb1, jb2 in tqdm(distances.values()):
        if max_connections is not None and connections == max_connections:
            break
        if jb1 not in remaining_jboxes and jb2 not in remaining_jboxes:
            jb1_circuit = None
            jb2_circuit = None
            for circuit in new_circuits:
                # Skip if both are on same circuit
                if jb1 in circuit and jb2 in circuit:
                    break
                # Merge circuits
                if jb1 in circuit and jb2 not in circuit:
                    jb1_circuit = circuit
                if jb2 in circuit and jb1 not in circuit:
                    jb2_circuit = circuit
                # End if found both circuits to merge
                if jb1_circuit and jb2_circuit:
                    break
            if jb1_circuit and jb2_circuit:
                new_circuits.remove(jb1_circuit)
                new_circuits.remove(jb2_circuit)
                new_circuits.append(jb1_circuit + jb2_circuit)
                connections += 1
                continue
        for circuit in new_circuits:
            if jb1 in circuit and jb2 not in circuit:
                if jb2 in remaining_jboxes:
                    circuit.append(jb2)
                    remaining_jboxes.remove(jb2)
            if jb2 in circuit and jb1 not in circuit:
                if jb1 in remaining_jboxes:
                    circuit.append(jb1)
                    remaining_jboxes.remove(jb1)
            if jb1 not in remaining_jboxes and jb2 not in remaining_jboxes:
                break
        if jb1 in remaining_jboxes and jb2 in remaining_jboxes:
            new_circuits.append([jb1, jb2])
            remaining_jboxes.remove(jb1)
            remaining_jboxes.remove(jb2)
        if jb1 in remaining_jboxes:
            new_circuits.append([jb1])
            remaining_jboxes.remove(jb1)
            continue
        if jb2 in remaining_jboxes:
            new_circuits.append([jb2])
            remaining_jboxes.remove(jb2)
            continue
        connections += 1
    return new_circuits


def part1(data: list[tuple(int, int, int)]):
    print("Running Part 1")
    distances = calculate_distances(data)
    new_circuits = make_circuits(data, distances, MAX_CONNECTIONS)

    new_circuits_lens = [len(x) for x in new_circuits]
    new_circuits_lens.sort(reverse=True)
    part1_result = math.prod(new_circuits_lens[:3])

    print(f"Part 1  = {part1_result}")


def part2(data: list[tuple(int, int, int)]):
    print("Running Part 2")
    distances = calculate_distances(data)
    new_circuits = make_circuits(data, distances, None)

    last_value = new_circuits[0][-1]
    # Get closes box to last one except self
    closest_to_last = sorted(data, key=lambda x: math.dist(x, last_value))[1]
    part2_result = last_value[0] * closest_to_last[0]

    print(f"Part 2  = {part2_result}")


if __name__ == "__main__":
    data = DATA.splitlines()
    data = [tuple(int(x) for x in r.split(",")) for r in data]
    part1(data)
    part2(data)
