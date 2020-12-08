import os


class Computer():
    def __init__(self):
        self.accumulator = 0
        self.current_step = 0

    def restart(self):
        self.accumulator = 0
        self.current_step = 0

    def modify_accumulator(self, value):
        self.accumulator += value
        self.current_step += 1

    def jump(self, value):
        self.current_step += value

    def do_nothing(self):
        self.current_step += 1

    def run(self, instructions):
        steps_done = []
        while self.current_step < len(instructions):
            # Return False on error (inifinite loop)
            if steps_done.count(self.current_step) == 2:
                return (False, self.accumulator)

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

        # Successful run
        return (True, self.accumulator)


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        instructions = f.read().splitlines()

    computer = Computer()

    for i in range(0, len(instructions)):
        computer.restart()
        new_instructions = instructions.copy()

        if 'jmp' in new_instructions[i]:
            new_instructions[i] = new_instructions[i].replace('jmp', 'nop')
        else:
            new_instructions[i] = new_instructions[i].replace('nop', 'jmp')

        return_value = computer.run(new_instructions)
        if return_value[0] == True:
            break

    print('Part 2 answer: ', return_value[1])


if __name__ == '__main__':
    main()
