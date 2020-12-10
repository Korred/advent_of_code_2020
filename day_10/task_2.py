from collections import Counter
from itertools import combinations

adapters = [int(line.strip()) for line in open("test_input.txt", "r")]
adapters.extend([0, max(adapters) + 3])
adapters.sort()
diffs = [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]

removable = [i + 1 for i in range(0, len(diffs) - 1) if diffs[i] + diffs[i + 1] <= 3]

"""
choices = []
for i in range(len(removable)):
    choices.extend([])
"""

print(removable)
print(diffs)
last = 0
groups = []
for e, d in enumerate(diffs):
    if d == 3:
        groups.append(adapters[last : e + 1])
        last = e + 1
        print(adapters[last])
groups.append([adapters[last]])

parts = []
for e, g in enumerate(groups):
    if len(g) <= 2:
        parts.append(1)
    elif len(g) == 3:
        parts.append(2)
    else:
        pass


"""
def get_counts(adapters):
    # can always return current adapter combination
    cnt = 1
    diffs = [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
    removable = [i + 1 for i in range(0, len(diffs) - 1) if diffs[i] + diffs[i + 1] <= 3]

    print(len(removable) ** 2 - 1)
    '''
    print(adapters)

    for r in removable:
        cnt += get_counts(adapters[:r] + adapters[r + 1 :])

    return cnt
    '''


print(get_counts(adapters))
"""
