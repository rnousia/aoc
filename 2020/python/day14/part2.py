import os
from itertools import product


def apply_bitmask(bitmask, value):

    binary_str = f'{value:036b}'
    bits = [bit for bit in binary_str]

    floating_positions = [i for value, i in bitmask if value == 'X']
    num_floating = len(floating_positions)

    for bitmask_value, index in bitmask:
        bits[index] = bitmask_value

    results = []
    # All possible combinations of 0 and 1
    replacements = list(product(range(2), repeat=num_floating))

    for replacement_bits in replacements:
        bits_copy = bits.copy()
        for i, position in enumerate(floating_positions):
            bits_copy[position] = str(replacement_bits[i])
        results.append(int(''.join(bits_copy), 2))

    return results


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        input_data = [line.split(' = ') for line in f.read().splitlines()]

    mem = {}

    for left_value, right_value in input_data:
        if left_value.startswith('mask'):
            bitmask = [(val, i)
                       for i, val in enumerate(right_value) if val != '0']
        else:
            address = int(''.join(filter(str.isdigit, left_value)))
            destination_addresses = apply_bitmask(bitmask, address)
            for address in destination_addresses:
                mem[address] = int(right_value)

    print('Part 2 answer: ', sum(mem.values()))


if __name__ == '__main__':
    main()
