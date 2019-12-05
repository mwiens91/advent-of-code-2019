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


def get_points(wire, step_dict):
    pointer = [0, 0]
    steps_pointer = 0
    points = []

    for move, x in wire:
        if move == UP:
            for i in range(1, x + 1):
                # Save the point
                point = (pointer[0], pointer[1] + i)
                points.append(point)

                # Save the number of steps
                if point not in step_dict:
                    step_dict[point] = steps_pointer + i

            # Adjust new pointer position
            pointer[1] += x
        elif move == DOWN:
            for i in range(1, x + 1):
                point = (pointer[0], pointer[1] - i)
                points.append(point)

                if point not in step_dict:
                    step_dict[point] = steps_pointer + i

            pointer[1] -= x
        elif move == LEFT:
            for i in range(1, x + 1):
                point = (pointer[0] - i, pointer[1])
                points.append(point)

                if point not in step_dict:
                    step_dict[point] = steps_pointer + i

            pointer[0] -= x
        else:
            for i in range(1, x + 1):
                point = (pointer[0] + i, pointer[1])
                points.append(point)

                if point not in step_dict:
                    step_dict[point] = steps_pointer + i

            pointer[0] += x

        steps_pointer += x

    return set(points)


# Count the number of steps to each point - these are changed in place
step_dict_1 = {}
step_dict_2 = {}

# Find intersections
intersections = get_points(wires[0], step_dict_1).intersection(
    get_points(wires[1], step_dict_2)
)

# Find min sum of steps intersection
times = [step_dict_1[point] + step_dict_2[point] for point in intersections]

print(min(times))
