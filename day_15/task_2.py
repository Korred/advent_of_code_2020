from collections import defaultdict, deque

numbers = list(map(int, open("input.txt", "r").read().strip().split(",")))
last_number_lkp = defaultdict(lambda: deque(maxlen=2))
limit = 30000000

for e, n in enumerate(numbers):
    last_number_lkp[n].append(e)

cnt = len(numbers)
while cnt < limit:
    n = numbers[-1]
    new_n = 0

    if n in last_number_lkp:
        if len(last_number_lkp[n]) == 2:
            new_n = abs(last_number_lkp[n][0] - last_number_lkp[n][1])

    last_number_lkp[new_n].append(cnt)
    numbers.append(new_n)

    cnt += 1
print(f"The 30000000th number spoken is: {numbers[-1]}")
