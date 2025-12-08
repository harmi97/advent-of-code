import math
from copy import deepcopy
from pathlib import Path

from tqdm import tqdm

DATA = Path(__file__.replace(".py", ".txt")).read_text()
MAX_CONNECTIONS = 1000


def part1(data: list[tuple(int, int, int)]):
    # Calculate distances
    distances = {}
    print("Calculating distances")
    for jbox in tqdm(data):
        other_jboxes = deepcopy(data)
        other_jboxes.remove(jbox)
        for other_jbox in other_jboxes:
            distance = math.dist(jbox, other_jbox)
            if distance in distances.keys() and distances[distance] != (
                other_jbox,
                jbox,
            ):
                raise ValueError
            distances[distance] = (jbox, other_jbox)

    # Construct circuits
    print("Making connections")
    remaining_jboxes = deepcopy(data)
    new_circuits = []
    distances = dict(sorted(distances.items()))
    connections = 0
    for jb1, jb2 in tqdm(distances.values()):
        if connections == MAX_CONNECTIONS:
            # if connections == 10:
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

    # pprint(distances)
    # pprint(sorted(new_circuits, key=len, reverse=True))
    new_circuits_lens = [len(x) for x in new_circuits]
    new_circuits_lens.sort(reverse=True)
    # print(new_circuits_lens)
    print(f"Part 1  = {math.prod(new_circuits_lens[:3])}")


if __name__ == "__main__":
    data = DATA.splitlines()
    data = [tuple(int(x) for x in r.split(",")) for r in data]
    part1(data)
