from collections import Counter

adapters = [int(line.strip()) for line in open("input.txt", "r")]
adapters.extend([0, max(adapters) + 3])
adapters.sort()
diffs = Counter([adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)])

print(f"Number of 1-jolt differences multiplied by the number of 3-jolt differences: {diffs[1]*diffs[3]}")
