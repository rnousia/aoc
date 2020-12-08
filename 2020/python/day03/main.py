import os
from functools import reduce


def count_trees(slope, x_step, y_step):
    trees = 0
    x = x_step

    pattern_length = len(slope[0])

    for i in range(y_step, len(slope), y_step):
        if slope[i][x % pattern_length] == '#':
            trees += 1
        x += x_step

    return trees


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        slope = f.read().splitlines()

    print('Part 1 answer: ', count_trees(slope, 3, 1))

    num_trees = [
        count_trees(slope, 1, 1),
        count_trees(slope, 3, 1),
        count_trees(slope, 5, 1),
        count_trees(slope, 7, 1),
        count_trees(slope, 1, 2)
    ]

    product_of_trees = reduce((lambda x, y: x * y), num_trees)
    print('Part 2 answer: ', product_of_trees)


if __name__ == '__main__':
    main()
