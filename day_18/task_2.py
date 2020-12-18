def shift_values(l, s, c=None):
    for i, v in enumerate(l):
        if c:
            if v > c:
                l[i] = v + s
        else:
            l[i] = v + s


def match_parentheses(l, i):
    pstack = [1]

    if l[i] == "(":
        for t in range(i + 1, len(l)):
            if l[t] == ")":
                pstack.pop()

            if l[t] == "(":
                pstack.append(1)

            if not pstack:
                return t
    else:
        for t in range(i - 1, -1, -1):
            if l[t] == ")":
                pstack.append(1)

            if l[t] == "(":
                pstack.pop()

            if not pstack:
                return t


def parse(expression):

    exp = list(expression.replace(" ", ""))
    add_idx = [i for i, e in enumerate(exp) if e == "+"]

    while add_idx:
        i = add_idx.pop(0)
        l, o, r = exp[i - 1 : i + 2]

        sub_exp = []
        if l.isnumeric():
            sub_exp.extend(["(", l, o])
        else:
            # parentheses ")"
            j = match_parentheses(exp, i - 1)
            exp = exp[:j] + ["("] + exp[j:]
            i += 1
            sub_exp.extend([l, o])

        # shift index by 1 (will always be shifted by 1)
        shift_values(add_idx, 1)

        if r.isnumeric():
            sub_exp.extend([r, ")"])

            # shift index by 1 (will always be shifted by 1)
            shift_values(add_idx, 1)
        else:
            # parentheses "("
            j = match_parentheses(exp, i + 1)
            exp = exp[:j] + [")"] + exp[j:]

            shift_values(add_idx, 1, j)

            sub_exp.extend([r])

        exp = exp[: i - 1] + sub_exp + exp[i + 2 :]

    return eval("".join(exp))


expressions = open("input.txt", "r").read().split("\n")

print(sum(map(parse, expressions)))
