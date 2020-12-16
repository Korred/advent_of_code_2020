from re import match

RE_FIELD = r"(^[\w ]+): (\d+)-(\d+) or (\d+)-(\d+)"
data = list(map(lambda x: x.split("\n"), open("input.txt", "r").read().split("\n\n")))

fields = {}

for field in data[0]:
    parts = match(RE_FIELD, field).groups()
    fields[parts[0]] = [range(int(parts[1]), int(parts[2]) + 1), range(int(parts[3]), int(parts[4]) + 1)]


my_ticket = tuple(map(int, data[1][1].split(",")))
nearby_tickets = [tuple(map(int, t.split(","))) for t in data[2][1:]]

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

print(sum([e[1] for e in invalid_numbers]))
