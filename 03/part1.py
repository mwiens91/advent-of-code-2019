#!/usr/bin/env python3

import sys

# Constants
UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

# Parse input
lines = [line.strip() for line in sys.stdin]
wires = [[(x[0], int(x[1:])) for x in line.split(",")] for line in lines]


def get_points(wire):
    pointer = [0, 0]
    points = []

    for move, x in wire:
        if move == UP:
            points += [(pointer[0], pointer[1] + i) for i in range(1, x + 1)]
            pointer[1] += x
        elif move == DOWN:
            points += [(pointer[0], pointer[1] - i) for i in range(1, x + 1)]
            pointer[1] -= x
        elif move == LEFT:
            points += [(pointer[0] - i, pointer[1]) for i in range(1, x + 1)]
            pointer[0] -= x
        else:
            points += [(pointer[0] + i, pointer[1]) for i in range(1, x + 1)]
            pointer[0] += x

    return set(points)


# Find intersections
intersections = get_points(wires[0]).intersection(get_points(wires[1]))

# Find min distance intersection
print(min([abs(x) + abs(y) for x, y in intersections]))
