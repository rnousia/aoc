import os


def is_valid_password(password, policy):
    locations, char_to_match = policy.split(' ')
    char_at_loc1, char_at_loc2 = [password[int(item)-1] for item in locations.split('-')]

    if (char_at_loc1 == char_to_match or char_at_loc2 == char_to_match) and char_at_loc1 != char_at_loc2:
        return True
    return False


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        items = f.read().splitlines()

    valid_count = 0
    for policy, password in [item.split(': ') for item in items]:
        if is_valid_password(password, policy):
            valid_count += 1

    print('Part 2 answer: ', valid_count)


if __name__ == '__main__':
    main()
