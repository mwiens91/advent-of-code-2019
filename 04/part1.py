#!/usr/bin/env python3

import sys

# Parse input
start, end = [int(x.strip()) for x in sys.stdin.read().split("-")]

# Count passwords
count = 0

for n in range(start, end + 1):
    n_list = list(str(n))

    if n_list != sorted(n_list):
        continue

    if len(set(n_list)) == 6:
        continue

    count += 1

# Print result
print(count)
