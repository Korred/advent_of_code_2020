import re

RE_INSTRUCTION = r"([\w]{3}) ([+\-\d]+)"


def execute_code(instructions):
    executed = set()
    accumulator = 0
    idx = 0

    while True:
        if idx in executed:
            return False

        if idx >= len(instructions):
            print(f"Accumulator value after program termination: {accumulator}")
            return True

        executed.add(idx)
        i = instructions[idx]

        if i[0] == "nop":
            idx += 1

        elif i[0] == "acc":
            accumulator += i[1]
            idx += 1

        elif i[0] == "jmp":
            idx += i[1]


def fix_code(instructions):
    to_replace = (("nop", "jmp"), ("jmp", "nop"))
    terminated = False

    for (cur, rep) in to_replace:
        if not terminated:
            cur_indices = [i for i, x in enumerate(instructions) if x[0] == cur]

            for idx in cur_indices:
                fixed_instructions = instructions[:]
                fixed_instructions[idx] = (rep, fixed_instructions[idx][1])
                terminated = execute_code(fixed_instructions)


instructions = []
with open("input.txt", "r") as data:
    for line in data:
        i = re.match(RE_INSTRUCTION, line.strip())
        instructions.append((i[1], int(i[2])))

fix_code(instructions)
