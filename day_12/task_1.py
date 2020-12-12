actions = [(lambda x: (x[0], int(x[1:])))(line.strip()) for line in open("input.txt", "r")]

dirs = ["N", "E", "S", "W"]
rot = "E"
moves = {"N": 0, "E": 0, "S": 0, "W": 0}

for a in actions:
    if a[0] in moves:
        moves[a[0]] += a[1]

    else:
        if a[0] == "R":
            rot = dirs[(dirs.index(rot) + (a[1] // 90)) % 4]
        if a[0] == "L":
            rot = dirs[(dirs.index(rot) - (a[1] // 90)) % 4]
        if a[0] == "F":
            moves[rot] += a[1]

distance = abs(moves["N"] - moves["S"]) + abs(moves["E"] - moves["W"])
print(f"(PART 1) Manhattan distance between end-location and the ship's starting position: {distance}")
