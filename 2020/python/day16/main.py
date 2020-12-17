import os
from itertools import permutations  


def split_list(input_list, separator):
    sub_list = []
    for item in input_list:
        if item == separator:
            yield sub_list
            sub_list = []
        else:
            sub_list.append(item)
    yield sub_list


def create_rules(notes):
    rules = {}
    for note in notes:
        key, rest = note.split(': ')
        range1, range2 = rest.split(' or ')
        rules[key] = { 'range1': [int(num) for num in range1.split('-')],
            'range2': [int(num) for num in range2.split('-')] }
    return rules

def is_in_range(value, value_range):
    if value_range:
        min_value, max_value = value_range
        if int(value) < min_value or int(value) > max_value:
            #print('Value {0} not in range {1}'.format(value, value_range))
            return False
    return True


def is_valid_value(ranges, value):
    return True if is_in_range(value, ranges[0]) or is_in_range(value, ranges[1]) else False
   

def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        lines = f.read().splitlines()

    notes = [item for item in split_list(lines, '')]

    # Parse input data
    rules = create_rules(notes[0])
    ticket_to_check = [[int(num) for num in note.split(',')] for note in notes[1][1:]][0]
    tickets = [[int(num) for num in note.split(',')] for note in notes[2][1:]]

    # Part 1
    invalid_values = []
    valid_tickets = tickets.copy()

    for ticket in tickets:
        for value in ticket:
            is_valid = False
            for key in rules:
                if is_valid_value((rules[key]['range1'], rules[key]['range2']), value):
                    is_valid = True
                    break
            if not is_valid:
                invalid_values.append(value)
                if ticket in valid_tickets:
                    valid_tickets.pop(valid_tickets.index(ticket))

    print('Part 1 answer: ', sum(invalid_values))
    
    # Part 2
    all_possible_positions = {}
    for key in rules:
        index = 0
        all_possible_positions[key] = []

        while index < len(rules):
            num_valid_values = 0

            for value_at_index in [ticket[index] for ticket in valid_tickets]:
                if not is_valid_value((rules[key]['range1'], rules[key]['range2']), value_at_index):
                    break
                else:
                    num_valid_values += 1
            
            if num_valid_values == len(valid_tickets):
                all_possible_positions[key].append(index)
            
            index += 1


    counts = {}
    for key in all_possible_positions:
        for i in all_possible_positions[key]:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
    

    positions = {}

    while len(all_possible_positions) > 0:
        for index in sorted(counts.items(), key = lambda x: x[1]):

            keys_at_index = []
            for key in all_possible_positions:
                if index in all_possible_positions[key]:
                    keys_at_index.append(key)
                    
            if len(keys_at_index) == 1:
                key = keys_at_index[0]
                positions[key] = index
                all_possible_positions.pop(key)


    # Calculate product values of keys starting with "departure"
    result = 1
    for key in positions:
        if key.startswith('departure'):
            result *= ticket_to_check[positions[key]]

    print('Part 2 answer: ', result)
    # result: 2564529489989


if __name__ == '__main__':
    main()
