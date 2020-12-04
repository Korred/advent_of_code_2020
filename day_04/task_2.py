import re

batch_data = []

# read input data
with open("input.txt", "r") as data:
    for p in data.read().split("\n\n"):
        batch_data.append(dict([entry.split(":") for entry in p.replace("\n", " ").split(" ")]))


RE_HEIGHT = r"^([\d]+)(in|cm)$"
RE_HAIRCL = r"^#[\da-f]{6}$"
RE_PASSID = r"^[\d]{9}$"
VLD_EYECL = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def validate_height(height_data):

    match = re.match(RE_HEIGHT, height_data)
    if match:
        height, unit = int(match.group(1)), match.group(2)

        if unit == "cm":
            return 150 <= height <= 193
        elif unit == "in":
            return 59 <= height <= 76

    return False


valid = 0
for passport in batch_data:
    s1 = set(passport.keys())
    s2 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
    s3 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

    if s1 == s2 or s1 == s3:
        try:
            assert 1920 <= int(passport["byr"]) <= 2002
            assert 2010 <= int(passport["iyr"]) <= 2020
            assert 2020 <= int(passport["eyr"]) <= 2030
            assert validate_height(passport["hgt"])
            assert re.match(RE_HAIRCL, passport["hcl"])
            assert passport["ecl"] in VLD_EYECL
            assert re.match(RE_PASSID, passport["pid"])
            valid += 1

        except AssertionError as e:
            pass


print(f"Valid passports after enhanced validation found: {valid}")

