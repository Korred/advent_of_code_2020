from math import prod

data = open("input.txt", "r").read().strip().split("\n")

buses = {int(b): e for e, b in enumerate(data[1].split(",")) if b != "x"}


found = False

t = 0
jump = list(buses.keys())[0]
matching = 1


while not found:

    all_valid = True
    t += jump
    matched = 0

    for b in buses:
        if ((t + buses[b]) % b) != 0:
            all_valid = False
            break
        else:
            matched += 1

    if all_valid:
        print(f"Solution: {t}")
        found = True

    if matched > matching:
        jump = prod(list(buses.keys())[:matched])

