actions = [(lambda x: (x[0], int(x[1:])))(line.strip()) for line in open("input.txt", "r")]


ship = {"N": 0, "E": 0, "S": 0, "W": 0}
waypoint = {"N": 1, "E": 10, "S": 0, "W": 0}


def rotate_waypoint(waypoint, direction, deg):
    dirs = ["N", "E", "S", "W"]
    new_waypoint = {}

    for d in dirs:
        if direction == "R":
            idx = (dirs.index(d) + (a[1] // 90)) % 4
        else:
            idx = (dirs.index(d) - (a[1] // 90)) % 4

        new_waypoint[dirs[idx]] = waypoint[d]

    return new_waypoint


for a in actions:
    if a[0] in waypoint:
        waypoint[a[0]] += a[1]
    else:
        if a[0] in ("R", "L"):
            waypoint = rotate_waypoint(waypoint, a[0], a[1])

        if a[0] == "F":
            for d in ship:
                ship[d] += waypoint[d] * a[1]

distance = abs(ship["N"] - ship["S"]) + abs(ship["E"] - ship["W"])
print(f"(PART 2) Manhattan distance between end-location and the ship's starting position: {distance}")
