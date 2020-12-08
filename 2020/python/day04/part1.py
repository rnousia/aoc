import os
import re


PASSPORT_POLICY = {
    'byr': {'required': True},
    'iyr': {'required': True},
    'eyr': {'required': True},
    'hgt': {'required': True},
    'hcl': {'required': True},
    'ecl': {'required': True},
    'pid': {'required': True},
    'cid': {'required': False},
}


def split_list(input_list, separator):
    sub_list = []
    for item in input_list:
        if item == separator:
            yield sub_list
            sub_list = []
        else:
            sub_list.append(item)
    yield sub_list


def parse_passport(passport):
    passport_dict = {}
    for item in passport:
        key, value = item.split(':')
        passport_dict[key] = value

    return passport_dict


def is_valid_passport(passport):
    for key in PASSPORT_POLICY:
        # Check required value exists
        if PASSPORT_POLICY[key]['required'] and key not in passport.keys():
            print('Reason to fail: required key {0} not found'.format(key))
            return False

    return True


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        lines = f.read().splitlines()
    valid_count = 0

    for passport in [' '.join(item).split(' ') for item in split_list(lines, '')]:
        parsed_passport = parse_passport(passport)
        if is_valid_passport(parsed_passport):
            valid_count += 1

    print('Part 1 answer: ', valid_count)


if __name__ == '__main__':
    main()
