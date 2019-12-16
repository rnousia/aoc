'''
The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off. Since the air conditioner can't vent its heat anywhere but back into the spacecraft, it's actually making the air inside the ship warmer.

Instead, you'll need to use the TEST to extend the thermal radiators. Fortunately, the diagnostic program (your puzzle input) is already equipped for this. Unfortunately, your Intcode computer is not.

Your computer is only missing a few opcodes:

Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Like all instructions, these instructions need to support parameter modes as described above.

Normally, after an instruction is finished, the instruction pointer increases by the number of values in that instruction. However, if the instruction modifies the instruction pointer, that value is used and the instruction pointer is not automatically increased.

For example, here are several programs that take one input, compare it to the value 8, and then produce one output:

3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:

3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
Here's a larger example:

3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
The above example program uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.

This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test, provide it 5, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one number, the diagnostic code.

What is the diagnostic code for system ID 5?
'''
import os

def parse_instructions(opcode):
    modes = [0, 0, 0]
    # Check if opcode has parameters
    if opcode > 10:
        # The opcode is the rightmost two digits of the first value in an instruction -> split params and save modes
        params = int(opcode / 100)
        params_len = len(str(params))
        modes = [int(x) for x in list(str(params)[params_len::-1])]
        if len(modes) < 3:
            modes.extend([0] * (3 - len(modes)))
        # Save the rightmost two digits as opcode
        opcode = int(str(opcode)[-2:])
    return opcode, modes

def run_computer(sequence, computer_options={}):
    integers = sequence.copy()
    index = 0
    opcode, modes = parse_instructions(integers[index])
    while opcode != 99:
        # Check which mode to use: position or immediate
        first_param = integers[integers[index+1]] if modes[0] == 0 and opcode != 3 else integers[index+1]
        if opcode in [1, 2]:
            # Check which mode to use: position or immediate
            second_param = integers[integers[index+2]] if modes[1] == 0 else integers[index+2]
            # Third parameter can't be in immediate mode
            third_param = integers[index+3]
            if opcode == 1:
                integers[third_param] = first_param + second_param
            else:
                integers[third_param] = first_param * second_param
            index += 4

        elif opcode == 3:
            if computer_options.get('input_values', None):
                integers[first_param] = computer_options['input_values'].pop(0)
            else:  
                integers[first_param] = int(input("Enter integer: "))
            index += 2
        elif opcode == 4:
            if computer_options.get('use_return', False):
                return first_param
            else:
                print(first_param)
            index += 2
        elif opcode in [5, 6]:
            # Check which mode to use: position or immediate
            second_param = integers[integers[index+2]] if modes[1] == 0 else integers[index+2]
            if opcode == 5 and first_param != 0:
                index = second_param
            elif opcode == 6 and first_param == 0:
                index = second_param
            else:
                index += 3
        elif opcode in [7, 8]:
            # Check which mode to use: position or immediate
            second_param = integers[integers[index+2]] if modes[1] == 0 else integers[index+2]
            # Third parameter can't be in immediate mode
            third_param = integers[index+3]
            if opcode == 7:
                integers[third_param] = 1 if first_param < second_param else 0
            else:
                integers[third_param] = 1 if first_param == second_param else 0
            index += 4
        else:
            print('Something went wrong...')
            break
        
        # Get the next opcode
        opcode, modes = parse_instructions(integers[index])

    return integers


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        code_sequence = [ int(code) for code in f.read().split(',')]

    run_computer(code_sequence)
    


if __name__== "__main__":
  main()

