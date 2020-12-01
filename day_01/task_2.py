from itertools import permutations
from math import prod

report = []

# read input data
with open("task_1_input.txt", "r") as data:
    for line in data:

        # remove entries that are too big
        entry = int(line.strip())
        if entry <= 2020:
            report.append(entry)

report.sort()

for p in permutations(report, 3):
    if sum(p) == 2020:
        print(f"Entries: {p}")
        print(f"Product: {prod(p)}")
        break
