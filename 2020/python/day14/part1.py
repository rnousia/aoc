import os


def apply_bitmask(bitmask, value):

    binary_str = f'{value:036b}'
    bits = [bit for bit in binary_str]

    for bitmask_value, index in bitmask:
        bits[index] = bitmask_value

    return int(''.join(bits), 2)


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        input_data = [line.split(' = ') for line in f.read().splitlines()]

    mem = {}

    for left_value, right_value in input_data:
        if left_value.startswith('mask'):
            bitmask = [(val, i)
                       for i, val in enumerate(right_value) if val != 'X']
        else:
            address = int(''.join(filter(str.isdigit, left_value)))
            mem[address] = apply_bitmask(bitmask, int(right_value))

    print('Part 1 answer: ', sum(mem.values()))


if __name__ == '__main__':
    main()
