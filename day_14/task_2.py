import re
from collections import defaultdict
from itertools import product

RE_WRITE = r"mem\[(\d+)] = (\d+)"

groups = list(map(lambda x: x.strip().split("\n"), open("input.txt", "r").read().strip().split("mask = ")[1:]))
bits = 36
memory = defaultdict(lambda: [0] * bits)


def apply_mask_v2(mask, val):
    addresses = []
    floating_x = product("01", repeat=sum([1 for x in mask if x == "X"]))

    for f in floating_x:
        add = val[:]
        choices = list(f)
        for e, b in enumerate(mask):
            if b == "1":
                add[e] = b
            elif b == "X":
                add[e] = choices.pop(0)
        addresses.append(int("".join(add), 2))

    return addresses


for g in groups:
    mask = g[0]
    for w in g[1:]:
        bin_add, bin_val = list(map(lambda x: list(format(int(x), "b").zfill(bits)), re.match(RE_WRITE, w).groups()))
        for add in apply_mask_v2(mask, bin_add):
            memory[add] = bin_val

mem_sum = sum(map(lambda x: int("".join(x), 2), memory.values()))
print(f"Sum of all values left in memory: {mem_sum}")
