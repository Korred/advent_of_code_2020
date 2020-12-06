from collections import Counter

groups = []

# read input data
with open("input.txt", "r") as data:
    for group in data.read().strip().split("\n\n"):
        members_cnt = group.count("\n") + 1
        yes_counter = Counter(group.replace("\n", ""))

        groups.append(len([1 for c in yes_counter if yes_counter[c] == members_cnt]))

print(f"Sum of questions that everyone answered YES to: {sum(groups)}")
