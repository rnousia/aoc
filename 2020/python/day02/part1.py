import os


def is_valid_password(password, policy):
    occurences, char_to_look = policy.split(' ')

    num_chars = password.count(char_to_look)
    if num_chars >= int(occurences.split('-')[0]) and num_chars <= int(occurences.split('-')[1]):
        return True
    return False


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        items = f.read().splitlines()

    valid_count = 0
    for policy, password in [item.split(': ') for item in items]:
        if is_valid_password(password, policy):
            valid_count += 1
    
    print('Part 1 answer: ', valid_count)


if __name__ == '__main__':
    main()
