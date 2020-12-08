import re

RE_INSTRUCTION = r"([\w]{3}) ([+\-\d]+)"


def execute_code(instructions):
    executed = set()
    accumulator = 0
    idx = 0

    while True:
        if idx in executed:
            print(f"Accumulator before loop execution: {accumulator}")
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


instructions = []
with open("input.txt", "r") as data:
    for line in data:
        i = re.match(RE_INSTRUCTION, line.strip())
        instructions.append((i[1], int(i[2])))


execute_code(instructions)
