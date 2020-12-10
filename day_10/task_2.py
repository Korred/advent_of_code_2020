from collections import Counter
from itertools import combinations

adapters = [int(line.strip()) for line in open("input.txt", "r")]
adapters.extend([0, max(adapters) + 3])
adapters.sort()

ways = {}
ways[0] = 1
for w in adapters[1:]:
    ways[w] = ways.get(w - 1, 0) + ways.get(w - 2, 0) + ways.get(w - 3, 0)

print(f"Total number of distinct ways: {ways[max(ways.keys())]}")

