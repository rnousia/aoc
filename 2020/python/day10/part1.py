import os


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        adapters = [int(line) for line in f.read().splitlines()]

    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()

    joltage_diff_counts = {1: 0, 2: 0, 3: 0}
    for i, adapter in enumerate(adapters):
        if i > 0:
            joltage_diff = adapter - adapters[i-1]
            if joltage_diff < 4:
                joltage_diff_counts[joltage_diff] += 0
            else:
                break

    print('Part 1 answer: ', joltage_diff_counts[1] * joltage_diff_counts[3])


if __name__ == '__main__':
    main()
