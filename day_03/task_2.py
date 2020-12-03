from dataclasses import dataclass
from math import prod


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Slope:
    right: int
    down: int


area_map = []

# read input data
with open("input.txt", "r") as data:
    for line in data:
        area_map.append(tuple(line.strip()))


slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]
trees_list = []

for slope in slopes:
    trees = 0
    pos = Position(0, 0)

    while pos.y < len(area_map):
        if area_map[pos.y][pos.x] == "#":
            trees += 1

        pos.x = (pos.x + slope.right) % len(area_map[0])
        pos.y += slope.down

    trees_list.append(trees)
    print(f"Number of trees encountered on {slope}: {trees}")

print(f"Product of trees: {prod(trees_list)}")
