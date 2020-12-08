import os
from itertools import combinations
from functools import reduce


def find_first_sum_of_combinations(values, sum_to_find, num_combinations):
    for combination in combinations(values, num_combinations):
        if sum(combination) == sum_to_find:
            return combination


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        lines = f.read().splitlines()
    
    expenses = [int(line) for line in lines]

    combination = find_first_sum_of_combinations(expenses, 2020, 3)
    result = reduce((lambda x, y: x * y), combination)

    print('Part 2 answer: ', result)


if __name__ == '__main__':
    main()
