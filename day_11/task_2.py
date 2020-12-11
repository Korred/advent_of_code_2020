import copy
from itertools import chain
from collections import Counter


def get_seat_status(layout, x, y):
    POSITIONS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    occupied = 0

    for p in POSITIONS:
        mul = 1
        while True:
            nx = x + (p[0] * mul)
            ny = y + (p[1] * mul)

            if 0 <= nx < len(layout[0]) and 0 <= ny < len(layout):
                if layout[ny][nx] == "#":
                    occupied += 1
                    break
                elif layout[ny][nx] == "L":
                    break
            else:
                break

            mul += 1

    if layout[y][x] == "L" and occupied == 0:
        return "#"
    elif layout[y][x] == "#" and occupied >= 5:
        return "L"
    else:
        return layout[y][x]


curr_layout = [list(line.strip()) for line in open("input.txt", "r")]

while True:
    new_layout = copy.deepcopy(curr_layout)
    for y, row in enumerate(curr_layout):
        for x, seat in enumerate(row):
            if seat in ("#", "L"):
                new_layout[y][x] = get_seat_status(curr_layout, x, y)

    if curr_layout == new_layout:
        print(f"Loop found - Occupied seats: {Counter(''.join(list(chain(*curr_layout))))['#']}")
        break
    else:
        curr_layout = new_layout
