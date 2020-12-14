import re
from collections import defaultdict

RE_WRITE = r"mem\[(\d+)] = (\d+)"

groups = list(map(lambda x: x.strip().split("\n"), open("input.txt", "r").read().strip().split("mask = ")[1:]))
bits = 36
memory = defaultdict(lambda: [0] * bits)


def apply_mask(mask, val):
    # inplace masking - no new list is created
    for e, b in enumerate(mask):
        if b != "X":
            val[e] = b

    return val


for g in groups:
    mask = g[0]
    for w in g[1:]:
        add, val = re.match(RE_WRITE, w).groups()
        memory[add] = apply_mask(mask, list(format(int(val), "b").zfill(bits)))

mem_sum = sum(map(lambda x: int("".join(x), 2), memory.values()))
print(f"Sum of all values left in memory: {mem_sum}")
