import os


def parse_menu_line(menu_line):
    ingredients, allergens = menu_line.split(' (contains ')

    return ingredients.split(' '), allergens.replace(')','').split(', ')


def find_food_containing_allergen(foods, allergen):
        return [food for food in foods if allergen in food['allergens']]


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        lines = f.read().splitlines()

    # Parse input data
    all_allergens = {}
    all_ingredients = {}
    foods = []

    for line in lines:
        food = {}
        ingredients, allergens = parse_menu_line(line)

        food['ingredients'] = set(ingredients)
        food['allergens'] = set(allergens)
        foods.append(food)

        for allergen in allergens:
            if allergen not in all_allergens.keys():
                all_allergens[allergen] = []
        
        for ingredient in ingredients:
            if ingredient not in all_ingredients.keys():
                all_ingredients[ingredient] = []
   
    

    for allergen in all_allergens.keys():
        foods_with_allergen = find_food_containing_allergen(foods, allergen)

        # Find common ingredient(s) for an allergen
        common_ingredients = set(foods_with_allergen.pop()['ingredients'])
        for food in foods_with_allergen:
            common_ingredients = common_ingredients & food['ingredients']
        
        all_allergens[allergen] = common_ingredients


    # Part 1
    ingredients_containing_allergens = []
    for ingredients in all_allergens.values():
        ingredients_containing_allergens.extend(ingredients)

    non_allergenic = []
    for ingredient in all_ingredients.keys():
        if ingredient not in ingredients_containing_allergens:
            non_allergenic.append(ingredient)

    count = 0
    for food in foods:
        for ingredient in non_allergenic:
            count += list(food['ingredients']).count(ingredient)
    
    
    print('Part 1 result:', count)
    # 2635


    # Part 2
    allergens = {}
    for allergen in all_allergens:
        allergens[allergen] = list(all_allergens[allergen])

    known_allergens = [allergen for allergen, ingredients in allergens.items() if len(ingredients) == 1]
    known_ingredients = [ingredients[0] for ingredients in allergens.values() if len(ingredients) == 1]
    
    while len(known_allergens) < len(allergens):
        for allergen, ingredients in allergens.items():
            if any([ingredient in known_ingredients for ingredient in ingredients]) and \
                allergen not in known_allergens:
                for known_ingredient in known_ingredients:
                    if known_ingredient in allergens[allergen]:
                        allergens[allergen].remove(known_ingredient)
        
        known_allergens = [allergen for allergen, ingredients in allergens.items() if len(ingredients) == 1]
        known_ingredients = [ingredients[0] for ingredients in allergens.values() if len(ingredients) == 1]
 
    
    print('Part 2 result:', ','.join([allergens[allergen][0] for allergen in sorted(allergens)]))
    # xncgqbcp,frkmp,qhqs,qnhjhn,dhsnxr,rzrktx,ntflq,lgnhmx


if __name__ == '__main__':
    main()
