#!/usr/bin/env python3

import functools
import sys

# Constants
ME = "YOU"
SANTA = "SAN"


def calculate_orbits(parent, depth):
    global visited

    # Keep track of what we've visited already
    visited.append(parent)

    # Print distance and exit
    if parent == SANTA:
        print(depth - 2)
        sys.exit(0)

    # Recurse
    for child in edge_map[parent]:
        if child not in visited:
            calculate_orbits(child, depth + 1)


# Parse input
lines = [line.strip() for line in sys.stdin]
direct_orbits = [line.split(")") for line in lines]
nodes = set(functools.reduce(lambda l, o: l + o, direct_orbits, []))

# Calculate edge map
edge_map = {node: [] for node in nodes}

for orbitee, orbiter in direct_orbits:
    edge_map[orbitee].append(orbiter)
    edge_map[orbiter].append(orbitee)

# Calculate number of direct + indirect orbits
visited = []
calculate_orbits(ME, 0)
