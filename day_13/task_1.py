data = open("input.txt", "r").read().strip().split("\n")
start = int(data[0])
buses = sorted([int(b) for b in data[1].split(",") if b != "x"])

found = False
t = start
while not found:
    for b in buses:
        if t % b == 0:
            print(f"Earliest bus at time {t} is bus: {b}")
            print(f"Solution: {(t-start)*b}")
            found = True

    t += 1
