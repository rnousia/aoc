import os


class Computer():
    def __init__(self):
        self.accumulator = 0
        self.current_step = 0

    def modify_accumulator(self, value):
        self.accumulator += value
        self.current_step += 1

    def jump(self, value):
        self.current_step += value

    def do_nothing(self):
        self.current_step += 1

    def debug(self, instructions):
        steps_done = []
        while steps_done.count(self.current_step) < 2:
            step = instructions[self.current_step]

            instruction, value = step.split(' ')
            value = int(value)

            if instruction == 'acc':
                self.modify_accumulator(value)
            elif instruction == 'jmp':
                self.jump(value)
            elif instruction == 'nop':
                self.do_nothing()

            steps_done.append(self.current_step)

        return self.accumulator


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        instructions = f.read().splitlines()

    computer = Computer()
    debug_value = computer.debug(instructions)

    # Part 1
    print('Part 1 answer: ', debug_value)


if __name__ == '__main__':
    main()
