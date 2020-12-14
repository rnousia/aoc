import os
import math


class Ferry():
    def __init__(self, angle, x=0, y=0):
        self.x = x
        self.y = y
        self.degrees = angle

    def move(self, operation, step):
        if operation in ('S', 'W', 'R', 'B'):
            step = -step

        if operation in ('N', 'S'):
            self.y += step
        elif operation in ('E', 'W'):
            self.x += step
        elif operation in ('F', 'B'):
            self.x += round(math.cos(math.radians(self.degrees)) * step)
            self.y += round(math.sin(math.radians(self.degrees)) * step)
        elif operation in ('L', 'R'):
            self.degrees += step


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        instructions = f.read().splitlines()

    ferry = Ferry(angle=0)

    for instruction in instructions:
        ferry.move(instruction[0], int(instruction[1:]))

    # Part 1
    print('Part 1 answer: ', abs(ferry.x - 0) + abs(ferry.y - 0))


if __name__ == '__main__':
    main()
