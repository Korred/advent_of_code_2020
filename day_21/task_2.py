from re import findall

data = open("input.txt", "r").read().split("\n")

food, allg_ing_mapping = list(), list()
ingredients, matched_ingredients, matched_allergens = set(), set(), set()
allergens_sets = dict()

for line in data:
    ings, allgs = map(lambda x: set(findall(r"[\w']+", x)), line[:-1].split(" (contains "))
    ingredients |= ings
    food.append((ings, allgs))

    for allergen in allgs:
        if allergen in allergens_sets and allergen not in matched_allergens:
            allergens_sets[allergen] &= set(ings)
            allergens_sets[allergen] -= matched_ingredients

            if len(allergens_sets[allergen]) == 1:
                allergens_to_remove = {allergen}

                while allergens_to_remove:
                    atr = allergens_to_remove.pop()
                    mi = allergens_sets[atr].pop()

                    matched_allergens.add(atr)
                    matched_ingredients.add(mi)

                    allg_ing_mapping.append([atr, mi])

                    for a in allergens_sets:
                        allergens_sets[a] -= matched_ingredients
                        if len(allergens_sets[a]) == 1:
                            allergens_to_remove.add(a)

        else:
            allergens_sets[allergen] = set(ings)

print(f"Canonical dangerous ingredient list: {','.join([x[1] for x in sorted(allg_ing_mapping, key=lambda x: x[0])])}")
