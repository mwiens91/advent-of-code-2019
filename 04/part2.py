#!/usr/bin/env python3

import sys

# Parse input
start, end = [int(x.strip()) for x in sys.stdin.read().split("-")]

# Count passwords
count = 0

for n in range(start, end + 1):
    n_list = list(str(n))
    n_list_set = set(n_list)

    if n_list != sorted(n_list):
        continue

    if len(n_list_set) == 6:
        continue

    if not any([n_list.count(x) == 2 for x in n_list_set]):
        continue

    count += 1

# Print result
print(count)
