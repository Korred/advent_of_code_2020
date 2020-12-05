boarding_passes = []

# read input data
with open("input.txt", "r") as data:
    for line in data:
        boarding_passes.append(tuple(line.strip()))

rows, cols = (128, 8)
ids = []

for bp in boarding_passes:
    cr, cc = map(list, (map(range, [rows, cols])))

    for c in bp:
        half_cr, half_cc = map(lambda x: x // 2, map(len, [cr, cc]))

        if c == "F":
            cr = cr[:half_cr]
        if c == "B":
            cr = cr[half_cr:]
        if c == "L":
            cc = cc[:half_cc]
        if c == "R":
            cc = cc[half_cc:]

    bp_id = (cr[0] * 8) + cc[0]
    ids.append(bp_id)


print(f"Highest seat ID: {max(ids)}")
