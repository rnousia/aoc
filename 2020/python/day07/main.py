import os


def create_rules_for_bags(instructions):
    bags = {}
    for instruction in instructions:
        bag, bags_inside = instruction.split(' bags contain ')
        bags[bag] = {}

        inner_bags = [bag for bag in bags_inside.split(', ')
                      if not 'no other bags' in bag]
        for inner_bag in inner_bags:
            splitted = inner_bag.split(' ')
            inner_bag = ' '.join(splitted[1:3])
            num_inner_bags = int(splitted[0])
            bags[bag][inner_bag] = num_inner_bags

    return bags


def find_containing_bags(all_bags, color_to_find):
    colors = []
    for unique_color in all_bags:
        for inner_bag_color in all_bags[unique_color]:
            if color_to_find == inner_bag_color:
                if unique_color not in colors:
                    colors.append(unique_color)
                    colors.extend(find_containing_bags(all_bags, unique_color))

    return list(set(colors))


def count_bags_inside_bag(all_bags, bag_color):
    total_num_bags = 0
    for inner_bag_color in all_bags[bag_color]:
        num_inner_bags = all_bags[bag_color][inner_bag_color]
        # Add number of inner bags to total
        total_num_bags += num_inner_bags
        # Count number of bags inside the inner bag and add to total
        total_num_bags += num_inner_bags * \
            count_bags_inside_bag(all_bags, inner_bag_color)

    return total_num_bags


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        instructions = f.read().splitlines()

    bags = create_rules_for_bags(instructions)

    # Part 1
    bags_containing_shiny_gold = find_containing_bags(
        bags, 'shiny gold')
    print('Part 1 answer:', len(bags_containing_shiny_gold))

    # Part 2
    num_of_bags = count_bags_inside_bag(bags, 'shiny gold')
    print('Part 2 answer:', num_of_bags)


if __name__ == '__main__':
    main()
