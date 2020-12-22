data = open("test_input.txt", "r").readlines()

food = []
for line in data:
    print(line[:-1].split(" (contains "))
    """
    ing, alg = map(lambda i, a: [i.split(" "), a.split(", ")], line[:-1].split("(contains"))
    print(ing, alg)
    """
