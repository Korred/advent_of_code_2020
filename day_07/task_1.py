from collections import defaultdict
import re


def count_outer(color, lkp):
    check = lkp[color]
    seen = set()

    while check:
        c = check.pop()
        seen.add(c)
        check.update(lkp[c])

    return len(seen)


bag_in = defaultdict(set)
bag_contains = defaultdict(list)

# read input data
with open("input.txt", "r") as data:
    for line in data:
        outer_color = re.match(r"(.+?) bags contain", line)[1]
        for cnt, inner_color in re.findall(r"(\d+) (.+?) bag[s]?[,.]", line):
            bag_in[inner_color].add(outer_color)
            bag_contains[outer_color].append((int(cnt), inner_color))

print(f"A SHINY GOLD bag is contained at least once in {count_outer('shiny gold', bag_in)} bags")
