#!/usr/bin/env python3

import functools
import sys


def calculate_orbits(parent, depth):
    global count

    for child in edge_map[parent]:
        count += 1 + depth

        calculate_orbits(child, depth + 1)


# Parse input
lines = [line.strip() for line in sys.stdin]
direct_orbits = [line.split(")") for line in lines]

# Find root
nodes = set(functools.reduce(lambda l, o: l + o, direct_orbits, []))
orbiters = [orbit[1] for orbit in direct_orbits]
root = (nodes - set(orbiters)).pop()

# Calculate edge map
edge_map = {node: [] for node in nodes}

for orbitee, orbiter in direct_orbits:
    edge_map[orbitee].append(orbiter)

# Calculate number of direct + indirect orbits
count = 0
calculate_orbits(root, 0)

# Print result
print(count)
