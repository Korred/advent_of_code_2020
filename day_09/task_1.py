from itertools import permutations

preamble = 25
numbers = [int(line.strip()) for line in open("input.txt", "r")]
invalid_num = None

for e, number in enumerate(numbers[preamble:]):
    sums = [sum(p) for p in permutations(numbers[e : e + preamble + 1], 2)]
    if number not in sums:
        invalid_num = number
        break

print(f"First number that does not have this property: {invalid_num}")
