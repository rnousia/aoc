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
import logging, sys

# 3rd party
import numpy as np

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

class Computer:
    def __init__(self, commands, mem_size=0):
        self.commands = commands
        self.opcode = None
        self.modes = [0, 0, 0]
        self.index = 0
        self.memory_buffer = np.zeros(mem_size)
        self.relative_base = 0

        # First opcode and modes
        self.__parse_current_instruction()

    def run(self):
        self.commands = np.append(np.array(self.commands), self.memory_buffer).astype(int)
        value = None
        while self.opcode != 99:
            logging.debug('At index {}, next four commands are: {}'
                .format(self.index, self.commands[self.index:self.index+4]))

            first_param = self.__get_value_based_on_mode(self.index+1, 0)
            second_param = self.__get_value_based_on_mode(self.index+2, 1)
            if len(self.commands) > self.index + 3:
                third_param = self.__get_value_based_on_mode(self.index+3, 2)

            logging.debug('At index {}, opcode is {} and parameters are: {}, {}, {}'
                .format(self.index, self.opcode, first_param, second_param, third_param))
            
            if self.opcode in [1, 2]:
                # Opcode 1 sums parameters
                if self.opcode == 1:
                    self.commands[third_param['addr']] = first_param['value'] + second_param['value']
                # Opcode 2 multiplies parameters
                else:
                    self.commands[third_param['addr']] = first_param['value'] * second_param['value']
                self.index += 4
            
            # Opcode 3 expects input and saves value
            elif self.opcode == 3:
                value = yield
                logging.info('Storing input %s' % value)
                self.commands[first_param['addr']] = value
                self.index += 2
            
            # Opcode 4 outputs value
            elif self.opcode == 4:
                logging.info('Yielding output %s' % first_param['value'])
                yield first_param['value']
                self.index += 2
            
            elif self.opcode in [5, 6]:
                # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction
                # pointer to the value from the second parameter. Otherwise, it does nothing.
                if self.opcode == 5 and first_param['value'] != 0:
                    self.index = second_param['value']
                # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction
                # pointer to the value from the second parameter. Otherwise, it does nothing.
                elif self.opcode == 6 and first_param['value'] == 0:
                    self.index = second_param['value']
                else:
                    self.index += 3
                
            elif self.opcode in [7, 8]:
                # Opcode 7 is less than: if the first parameter is less than the second parameter,
                # it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
                if self.opcode == 7:
                    self.commands[third_param['addr']] = 1 if first_param['value'] < second_param['value'] else 0
                # Opcode 8 is equals: if the first parameter is equal to the second parameter,
                # it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
                else:
                    self.commands[third_param['addr']] = 1 if first_param['value'] == second_param['value'] else 0
                self.index += 4
            
            # Opcode 9 adjusts the relative base
            elif self.opcode == 9:
                self.relative_base += first_param['value']
                self.index += 2
            else:
                raise ValueError('invalid opcode: %s' % self.opcode)
            
            # Get the next opcode
            self.__parse_current_instruction()

    def __parse_current_instruction(self):
        modes = [0, 0, 0]
        opcode = self.commands[self.index]
        # Check if opcode has parameters
        if opcode > 10:
            # The opcode is the rightmost two digits of the first value in an instruction -> split params and save modes
            params = int(opcode / 100)
            params_len = len(str(params))
            modes = [int(x) for x in list(str(params)[params_len::-1])]
            # Get modes for three parameters, default to 0
            if len(modes) < 3:
                modes.extend([0] * (3 - len(modes)))
            # Save the rightmost two digits as opcode
            opcode = int(str(opcode)[-2:])
        
        logging.debug('Parsing instruction {}, opcode is {} with mode {}'
            .format(self.commands[self.index], opcode, ','.join([str(x) for x in modes])))
        
        self.opcode = opcode
        self.modes = modes


    def __get_value_based_on_mode(self, index, modes_index):
        value = self.commands[index]
        mode = self.modes[modes_index]

        return_value = None
        # Position mode, use value as address
        if mode == 0:
            try:
                return_value = self.commands[value]
            except IndexError:
                pass
        # Immediate mode does not change value
        elif mode == 1:
            return_value = value
        # Relative base mode, adjust address with offset and return value at address
        elif mode == 2:
            value += self.relative_base
            try:
                return_value = self.commands[value]
            except IndexError:
                pass
        # Return also immediate mode value to be used as address if needed
        return { 'value': return_value, 'addr': value }


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        code_sequence = [ int(code) for code in f.read().split(',')]

    computer = Computer(code_sequence).run()
    output = None
    for step in computer:
        if not output:
            output = computer.send(int(input('Enter integer:')))
        else:
            output = step
        if output:
            print(output)
    


if __name__== '__main__':
  main()

