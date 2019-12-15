#!/usr/bin/env python3

import math
import re
import sys

# Recipe dict constants
FUEL = "FUEL"
ORE = "ORE"
NUM = "num"
REACTANTS = "reactants"

# Parse input
lines = [line.strip() for line in sys.stdin]

# Find recipes
recipes = {}

for line in lines:
    matches = re.findall(r"(\d+ \w+)", line)

    product = matches[-1].split()
    product_num = int(product[0])
    product_name = product[1]

    reactants = matches[:-1]
    reactants_split = [r.split() for r in reactants]

    recipes[product_name] = {
        NUM: product_num,
        REACTANTS: {r[1]: int(r[0]) for r in reactants_split},
    }

# Find how much ore we need
resources_required = {
    **{ORE: 0},
    **{key: 1 if key == FUEL else 0 for key in recipes},
}
excess_resources = {key: 0 for key in recipes}

while True:
    temp_required = {
        **{ORE: resources_required[ORE]},
        **{key: 0 for key in recipes},
    }
    only_ore = True

    for resource, quantity in resources_required.items():
        if resource == ORE:
            continue

        if quantity:
            # Take away from excess if we have any
            excess_taken = min(excess_resources[resource], quantity)
            excess_resources[resource] -= excess_taken

            new_quantity = quantity - excess_taken

            if not new_quantity:
                continue

            # Determine quantity of reactants required
            only_ore = False

            multiplier = math.ceil(new_quantity / recipes[resource][NUM])
            excess_resources[resource] += (
                recipes[resource][NUM] * multiplier - new_quantity
            )

            for reactant, num in recipes[resource][REACTANTS].items():
                temp_required[reactant] += num * multiplier

    resources_required = temp_required

    if only_ore:
        break

# Print answer
print(resources_required[ORE])
