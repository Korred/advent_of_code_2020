numbers = list(map(int, open("input.txt", "r").read().strip().split(",")))
last_lkp = {n: i for i, n in enumerate(numbers)}
steps = 30000000

last_num = numbers[-1]
for i in range(len(numbers) - 1, steps - 1):
    new_num = i - last_lkp.get(last_num, i)
    last_lkp[last_num] = i
    last_num = new_num

print(f"The 30000000th number spoken is: {last_num}")
