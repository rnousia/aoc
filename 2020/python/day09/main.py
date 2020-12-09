import os
from itertools import combinations


def find_exception(preamble_length, numbers):
    for i, number in enumerate(numbers):
        if i >= preamble_length:
            if not is_sum_of_two_numbers(number, numbers[i-preamble_length:i]):
                return number
    return None


def is_sum_of_two_numbers(sum_value, numbers):
    for combination in combinations(numbers, 2):
        if sum_value == sum(combination):
            return True
    return False


def find_contiguos_set(sum_to_find, numbers):
    for i in range(0, len(numbers)):

        for j in range(i+1, len(numbers)):
            sequence_to_check = numbers[i:j]
            if sum(sequence_to_check) == sum_to_find:
                return min(sequence_to_check) + max(sequence_to_check)
            elif sum(sequence_to_check) > sum_to_find:
                break

    return None


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        input_numbers = [int(line) for line in f.read().splitlines()]

    preamble_length = 25
    invalid_value = find_exception(preamble_length, input_numbers)
    print('Part 1 answer: ', find_exception(preamble_length, input_numbers))

    if invalid_value:
        print('Part 2 answer: ', find_contiguos_set(
            invalid_value, input_numbers))


if __name__ == '__main__':
    main()
