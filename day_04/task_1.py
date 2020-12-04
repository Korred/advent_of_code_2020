batch_data = []

# read input data
with open("input.txt", "r") as data:
    for p in data.read().split("\n\n"):
        batch_data.append(dict([entry.split(":") for entry in p.replace("\n", " ").split(" ")]))

valid = 0
for passport in batch_data:
    s1 = set(passport.keys())
    s2 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
    s3 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

    if (s1 == s2) or (s1 == s3):
        valid += 1

print(f"Valid passports found: {valid}")
