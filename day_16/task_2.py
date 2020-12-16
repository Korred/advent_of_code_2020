from re import match
from math import prod

RE_FIELD = r"(^[\w ]+): (\d+)-(\d+) or (\d+)-(\d+)"
data = list(map(lambda x: x.split("\n"), open("input.txt", "r").read().split("\n\n")))

fields = {}

for field in data[0]:
    parts = match(RE_FIELD, field).groups()
    fields[parts[0]] = [range(int(parts[1]), int(parts[2]) + 1), range(int(parts[3]), int(parts[4]) + 1)]


my_ticket = tuple(map(int, data[1][1].split(",")))
nearby_tickets = [tuple(map(int, t.split(","))) for t in data[2][1:]]

# filter out invalid tickets by finding numbers that do not fit in any range
invalid_numbers = []
for e, ticket in enumerate(nearby_tickets):
    for number in ticket:
        matched = False
        for f in fields:
            for r in fields[f]:
                if number in r:
                    matched = True

        if not matched:
            invalid_numbers.append((e, number))

for n in reversed(invalid_numbers):
    del nearby_tickets[n[0]]


# find possible valid fields and certain invalid fields
valid = {i: set() for i in range(len(fields))}
invalid = {i: set() for i in range(len(fields))}

for f in fields:
    for ticket in nearby_tickets:
        for e, number in enumerate(ticket):

            if number in fields[f][0] or number in fields[f][1]:
                valid[e].add(f)
            else:
                invalid[e].add(f)


# remove invalid fields set from valid fields set
candidates = {n: valid[n] - invalid[n] for n in valid}

# find candidates with only one element and remove this element from all other sets
# repeat until every set contains only one element
to_remove = set()
i = 0
while True:
    found = False
    for c in candidates:

        if len(candidates[c]) != 1:
            candidates[c] -= to_remove
        if len(candidates[c]) == 1:
            field = list(candidates[c])[0]
            if field not in to_remove:
                found = True
                to_remove.add(field)
        else:
            candidates[c] -= to_remove

    i += 1
    if not found:
        break

print(prod([my_ticket[c] for c in candidates if "departure" in list(candidates[c])[0]]))
