from collections import deque


def main():
    # input
    starting_numbers = [16, 1, 0, 18, 12, 14, 19]

    all_numbers = {}
    last_number = None

    for i, number in enumerate(starting_numbers):
        all_numbers[number] = {'count': 1, 'index': deque([i])}
        last_number = number

    for i in range(len(starting_numbers), 2020):
        if all_numbers[last_number]['count'] > 1:
            number = all_numbers[last_number]['index'][-1] - \
                all_numbers[last_number]['index'][-2]
            if number in all_numbers:
                all_numbers[number]['count'] += 1
                all_numbers[number]['index'].append(i)
                if all_numbers[number]['count'] > 2:
                    all_numbers[number]['index'].popleft()
            else:
                all_numbers[number] = {'count': 1, 'index': deque([i])}
            last_number = number

        else:
            all_numbers[0]['count'] += 1
            all_numbers[0]['index'].append(i)
            last_number = 0

    print('Part 1 answer: ', last_number)


if __name__ == '__main__':
    main()
