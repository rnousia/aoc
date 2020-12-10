import os


def count_num_arrangements(adapters, max_chained_adapters=3, max_joltage_diff=3):
    # Add charging outlet rating to data
    adapters.append(0)
    # Add built-in adapter rating to data
    adapters.append(max(adapters) + max_joltage_diff)
    adapters.sort()

    adapter_counts = {}
    for i, adapter in enumerate(adapters):
        if i == 0:
            adapter_counts[adapter] = 1
        else:
            adapter_counts[adapter] = adapter_counts[adapters[i-1]]
            # Number of previous adapters to consider
            n = min(i, max_chained_adapters)

            for previous_adapter in adapters[i-n:i-1]:
                if is_compatible_adapter(adapter, previous_adapter, max_joltage_diff):
                    # Clone existing arrangemets and save total (only latest count is updated)
                    adapter_counts[adapter] += adapter_counts[previous_adapter]

    return adapter_counts[max(adapters)]


def is_compatible_adapter(first_adapter, second_adapter, max_joltage_diff):
    joltage_diff = first_adapter - second_adapter
    if joltage_diff <= max_joltage_diff:
        return True
    return False


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        adapters = [int(line) for line in f.read().splitlines()]

    print('Part 2 answer: ', count_num_arrangements(adapters))


if __name__ == '__main__':
    main()
