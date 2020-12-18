import os
import operator

OPERATORS = { '+': operator.add, '*': operator.mul }


def do_homework(homework, advanced=False):
    fragments = [ char for char in homework.replace(' ','')]
    if advanced:
        return calculate_expression_with_advanced_math(fragments)
    return calculate_expression(fragments)


def calculate_expression(expression):
    left_operand, right_operand, operator_key = None, None, None

    i = 0
    while i < len(expression):
        fragment = expression[i]

        if fragment in ('+','*'):
            operator_key = fragment
    
        elif fragment.isnumeric():
            if not left_operand:
                left_operand = fragment
            else:
                right_operand = fragment

        elif fragment == '(':
            right_operand, j = calculate_expression(expression[i+1:])
            if not left_operand:
                left_operand = right_operand
                right_operand = None
            i += j
        
        elif fragment == ')':
            return left_operand, i + 1
        
        if left_operand and right_operand and operator_key:
            left_operand = calculate(int(left_operand),int(right_operand), operator_key)
            right_operand, operator_key = None, None

        i += 1
    
    return int(left_operand), i

def calculate_expression_with_advanced_math(expression):
    left_operand, right_operand, operator_key = None, None, None

    i = 0
    while i < len(expression):
        fragment = expression[i]
    
        if fragment == '+':
            operator_key = fragment
        
        elif fragment == '*':
            operator_key = fragment
            right_operand, j = calculate_expression_with_advanced_math(expression[i+1:])
            i += j
        
        elif fragment.isnumeric():
            if not left_operand:
                left_operand = fragment
            else:
                right_operand = fragment

        elif fragment == '(':
            right_operand, j = calculate_expression_with_advanced_math(expression[i+1:])
            if not left_operand:
                left_operand = right_operand
                right_operand = None
            i += j
        
        elif fragment == ')':
            return left_operand, i + 1
        
        if left_operand and right_operand and operator_key:
            left_operand = calculate(int(left_operand), int(right_operand), operator_key)
            if operator_key == '*':
                return left_operand, i + 1
            right_operand, operator_key = None, None
        
        i += 1
    
    return int(left_operand), i

def calculate(left_operand, right_operand, operator_key):
    return OPERATORS[operator_key](left_operand, right_operand)


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        homework = f.read().splitlines()

    answers = []
    for expression in homework:
        answers.append(do_homework(expression)[0])
    
    print('Part 1 answer: ', sum(answers))
    # result: 6923486965641

    # Part 2
    answers = []
    for expression in homework:
        answers.append(do_homework(expression, advanced=True)[0])

    print('Part 2 answer: ', sum(answers))
    # result: 70722650566361


if __name__ == '__main__':
    main()
