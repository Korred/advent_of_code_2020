groups = []

# read input data
with open("input.txt", "r") as data:
    for group in data.read().split("\n\n"):
        yes_set = set(group.replace("\n", ""))
        groups.append(yes_set)

print(f"Sum of questions that anyone answered YES to: {sum(map(len, groups))}")
