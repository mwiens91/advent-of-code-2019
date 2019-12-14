#!/usr/bin/env python3

import math
import sys

# Constants
ASTEROID = "#"
EMPTY = "."

# Parse input
lines = [line.strip() for line in sys.stdin]
points = []

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == ASTEROID:
            points.append((row, col))

# Calculate the best asteroid
best = 0
best_point = ()
best_angle_dict = {}

for parent in points:
    angle_dict = {}

    for child in points:
        if child == parent:
            continue

        angle = math.atan2(parent[0] - child[0], child[1] - parent[1])

        if angle in angle_dict:
            angle_dict[angle] += [child]
        else:
            angle_dict[angle] = [child]

    if (num_angles := len(angle_dict.keys())) > best:
        best = num_angles
        best_point = parent
        best_angle_dict = angle_dict

# Rename var for convenience
angle_dict = best_angle_dict

# Sort each asteroid in list by furthest distance
for points in angle_dict.values():
    points.sort(key=lambda p: math.dist(p, best_point))

# Order the angles starting at pi/2 going clockwise
sorted_angles = sorted(
    angle_dict.keys(),
    key=lambda a: a if a <= math.pi / 2 else a - 2 * math.pi,
    reverse=True,
)

# Determine the 200th asteroid
count = 0
done = False

while True:
    if done:
        break

    for angle in sorted_angles:
        if count >= 200:
            done = True
            break

        if angle_dict[angle]:
            target = angle_dict[angle].pop(0)
            count += 1

# Print answer
print(100 * target[1] + target[0])
