'''
You now have a complete Intcode computer.

Finally, you can lock on to the Ceres distress signal! You just need to boost your sensors using the BOOST program.

The program runs in sensor boost mode by providing the input instruction the value 2. Once run, it will boost the sensors automatically, but it might take a few seconds to complete the operation on slower hardware. In sensor boost mode, the program will output a single value: the coordinates of the distress signal.

Run the BOOST program in sensor boost mode. What are the coordinates of the distress signal?
'''
import os
import itertools

from day5.part2 import Computer


def run_program(input_sequence, input_value=None):
    output = []
    computer = Computer(input_sequence.copy(), mem_size=2000).run()

    for step in computer:
        if not step:
            output.append(computer.send(input_value))
        else:
            output.append(step)
    return output if len(output) > 1 else output[0]


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        code_sequence = [ int(code) for code in f.read().split(',')]

    output = run_program(code_sequence, 2)
    print(output)

  
if __name__== '__main__':
  main()
