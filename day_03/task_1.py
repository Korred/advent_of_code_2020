from dataclasses import dataclass


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

slope = Slope(3, 1)
trees = 0
pos = Position(0, 0)

while pos.y < len(area_map):
    if area_map[pos.y][pos.x] == "#":
        trees += 1

    pos.x = (pos.x + slope.right) % len(area_map[0])
    pos.y += slope.down


print(f"Number of trees encountered on {slope}: {trees}")
