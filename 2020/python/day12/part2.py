import os
import math


class Ferry():
    def __init__(self, waypoint_x, waypoint_y):
        self.x = 0
        self.y = 0
        self.waypoint = Waypoint(waypoint_x, waypoint_y)

    def apply_instruction(self, instruction, value):
        if instruction in ('N', 'S', 'E', 'W'):
            self.waypoint.move(instruction, value)

        elif instruction == 'F':
            self.x += value * self.waypoint.x
            self.y += value * self.waypoint.y

        elif instruction in ('L', 'R'):
            self.waypoint.turn(instruction, value)


class Waypoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = calculate_distance(x, y)
        self.angle = calculate_angle(x, y)

    def move(self, direction, value):
        if direction == 'N':
            self.y += value
        elif direction == 'S':
            self.y -= value
        elif direction == 'E':
            self.x += value
        elif direction == 'W':
            self.x -= value

        self.distance = calculate_distance(self.x, self.y)
        self.angle = calculate_angle(self.x, self.y)

    def turn(self, direction, value):
        if direction == 'L':
            self.angle += value
        elif direction == 'R':
            self.angle -= value

        self.x = round(math.cos(math.radians(self.angle)) * self.distance)
        self.y = round(math.sin(math.radians(self.angle)) * self.distance)


def calculate_angle(x, y):
    if x == 0:
        return 90 if y > 0 else -90
    elif y == 0:
        return 0 if x > 0 else 180

    angle = math.degrees(math.atan(y/x))
    if x < 0:
        return 180 + angle if y >= 0 else angle - 180

    return angle


def calculate_distance(x, y):
    return math.sqrt(pow(x, 2) + pow(y, 2))


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        instructions = f.read().splitlines()

    ferry = Ferry(10, 1)

    for instruction in instructions:
        ferry.apply_instruction(instruction[0], int(instruction[1:]))

    print('Part 2 answer: ', abs(ferry.x - 0) + abs(ferry.y - 0))


if __name__ == '__main__':
    main()
