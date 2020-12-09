from itertools import combinations, permutations

preamble = 25
numbers = [int(line.strip()) for line in open("input.txt", "r")]
invalid_num = None

for e, number in enumerate(numbers[preamble:]):
    sums = [sum(p) for p in permutations(numbers[e : e + preamble + 1], 2)]
    if number not in sums:
        invalid_num = number
        break


def contiguous_numbers(numbers, length):
    s, e = 0, length
    while e != len(numbers):
        yield numbers[s:e]
        s += 1
        e += 1


length = 2
found = False
while not found:
    for c in contiguous_numbers(numbers, length):
        if sum(c) == invalid_num:
            print(f"Encryption weakness in XMAS-encrypted list: {sum([min(c),max(c)])}")
            found = True
            break

    length += 1
