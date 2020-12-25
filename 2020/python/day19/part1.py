import os
import re


class MessageValidator():
    def __init__(self, id):
        self.id = id
        self.validators = []
        self.valid_format = None
        self.validator = None
        self.message = ''
    
    def add_validator(self, validator):
        self.validators.append(validator)
    
    def create_validator(self, value):
        self.valid_format = value
        self.validator = lambda value, format: has_valid_format(value, format)
    
    def validate(self, recursion_level=0):
        results = []
        sub_results = []

        # Check that message has correct length
        if len(self.message) != self.count_validators():
            #print('message is too long/short, message len', len(self.message), 'not', self.count_validators())
            return False
        
        i = 0
        if self.validator:
            results.append(self.validator(self.message[i], self.valid_format))
            i += 1

    
        for validator in self.validators:
            if isinstance(validator, MessageValidator) and validator.validator:
                result = validator.validator(self.message[i], validator.valid_format)
                results.append(result)
                i += 1
            elif isinstance(validator, MessageValidator):
                validator.message = self.message[i:i+validator.count_validators()]
                results.append(validator.validate(recursion_level+1))
                i += validator.count_validators()
            else:
                if isinstance(validator, list):  
                    sub_results = []
                    j = 0
                    for sub_validator in validator:
                        sub_validator.message = self.message[j:j+sub_validator.count_validators()]
                        sub_results.append(sub_validator.validate())
                        j += sub_validator.count_validators()

                    results.append(all(sub_results))
        
        # Detect if rule has sub results (any true result means meassage part is valid)
        if len(results) > i:
            results = [any(results)]

        return all(results)

    def count_validators(self):
        count = 0
        if self.validator:
            count += 1
        else:
            for validator in self.validators:
                if isinstance(validator, MessageValidator) and validator.validator:
                    count += 1
                elif isinstance(validator, MessageValidator):
                    count += validator.count_validators()
                elif isinstance(validator, list):
                    for sub_validator in validator:
                        count += sub_validator.count_validators() / 2
        return int(count)
 

def create_message_validators(rules):
    validators = {}
    validation_rules = {}

    # Validators
    for id, params in [rule.split(': ') for rule in rules]:
        validators[id] = (MessageValidator(id))
        if params.startswith('"'):
            validators[id].create_validator(params.replace('"',''))
        else:
           validation_rules[id] = params
    
    validator_objects = validators.values()
    
    # More complex validator with sub rules
    for validator in validator_objects:
        if not validator.validator:
            sub_rules = [item for item in validation_rules[validator.id].split(' | ')]
            if len(sub_rules) == 1:
                for sub_validator_id in sub_rules[0].split(' '):
                    validator.add_validator(validators[sub_validator_id])
            else:
                for sub_rule in sub_rules:
                    validator.add_validator([validators[id] for id in sub_rule.split(' ')])

    return validators


def has_valid_format(value, value_format):
    if value_format and not re.search(value_format, value):
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


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        lines = f.read().splitlines()

    # Parse input
    rules, messages = [item for item in split_list(lines, '')]
    validators = create_message_validators(rules)
 
    results = []
    for message in messages:
        validators['0'].message = message
        results.append(validators['0'].validate())

    print('Part 1 answer:', len([res for res in results if res]))


if __name__ == '__main__':
    main()
