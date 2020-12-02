from dataclasses import dataclass


@dataclass
class Password:
    lo: int
    hi: int
    letter: str
    password: str


pw_list = []

# read input data
with open("input.txt", "r") as data:
    for line in data:
        parts = line.strip().split()
        cnts = tuple(map(int, parts[0].split("-")))
        pw_list.append(Password(cnts[0], cnts[1], parts[1][0], parts[2]))

valid_pw = 0
for line in pw_list:
    pos_str = line.password[line.lo - 1] + line.password[line.hi - 1]
    if pos_str.count(line.letter) == 1:
        valid_pw += 1

print(f"Number of valid passwords found: {valid_pw}")
