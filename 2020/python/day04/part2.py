import os
import re


PASSPORT_POLICY = {
    'byr': {'required': True,
            'validator': lambda x: has_valid_format(x, r'^\d{4}$') and is_in_range(x, [1920, 2020])
            },
    'iyr': {'required': True,
            'validator': lambda x: has_valid_format(x, r'^\d{4}$') and is_in_range(x, [2010, 2020])
            },
    'eyr': {'required': True,
            'validator': lambda x: has_valid_format(x, r'^\d{4}$') and is_in_range(x, [2020, 2030])
            },
    'hgt': {'required': True,
            'validator': lambda x: (has_valid_format(x, r'^\d+cm$') and is_in_range(re.match(r'^\d+', x).group(), [150, 193]))
            or (has_valid_format(x, r'^\d+in$') and is_in_range(re.match(r'^\d+', x).group(), [59, 76]))
            },
    'hcl': {'required': True,
            'validator': lambda x: has_valid_format(x, r'^#[a-f0-9]{6}$')
            },
    'ecl': {'required': True,
            'validator': lambda x: has_valid_format(x, r'^[a-z]{3}$')
            and is_in_values(x, ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
            },
    'pid': {'required': True, 'validator': lambda x: has_valid_format(x, r'^\d{9}$')
            },
    'cid': {'required': False, 'validator': None}
}


def has_valid_format(value, value_format):
    if value_format and not re.search(value_format, value):
        print('Value {0} has incorrect format, should be {1}'.format(
            value, value_format))
        return False
    return True


def is_in_range(value, value_range):
    if value_range:
        min_value, max_value = value_range
        if int(value) < min_value or int(value) > max_value:
            print('Value {0} not in range {1}'.format(value, value_range))
            return False
    return True


def is_in_values(value, values):
    if values and value not in values:
        print('Value {0} not in list {1}'.format(value, values))
        return False
    return True


def split_list(input_list, separator):
    sub_list = []
    for item in input_list:
        if item == separator:
            yield sub_list
            sub_list = []
        else:
            sub_list.append(item)
    yield sub_list


def parse_passpord(passport_items):
    passport_dict = {}
    for item in passport_items:
        key, value = item.split(':')
        passport_dict[key] = value

    return passport_dict


def is_valid_passport(passport):
    for key in PASSPORT_POLICY:
        # Check that required key exists
        if PASSPORT_POLICY[key]['required'] and key not in passport.keys():
            print('Required key {0} not found'.format(key))
            return False
        # Check values
        else:
            validator = PASSPORT_POLICY[key]['validator']
            if validator and not validator(passport[key]):
                return False

    return True


def count_valid_passports(passports):
    valid_count = 0
    for passport in passports:
        if is_valid_passport(passport):
            valid_count += 1
    return valid_count


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        lines = f.read().splitlines()

    # Parse passports from input
    passports = [parse_passpord(' '.join(item).split(' '))
                 for item in split_list(lines, '')]

    print('Part 2 answer: ', count_valid_passports(passports))


if __name__ == '__main__':
    main()
