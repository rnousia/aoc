'''
The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?
'''
import os


def print_panel(matrix):
    print('\n'.join([''.join([item for item in row]) for row in matrix]))

def follow_wire(wire_panel, directions, start_x, start_y, wire_mark):
    current_x = start_x
    current_y = start_y
    for direction in directions:
        print(direction)
        distance = int(direction[1:])
        x_factor = 0
        y_factor = 0
        if direction[0] == 'R':
            x_factor = 1
        elif direction[0] == 'L':
            x_factor = -1
        elif direction[0] == 'U':
            y_factor = -1
        elif direction[0] == 'D':
            y_factor = 1

        for step in range(distance - 1):
            current_x += x_factor * 1
            current_y += y_factor * 1
            if wire_panel[current_y][current_x] == '.':
                wire_panel[current_y][current_x] = wire_mark
            elif wire_panel[current_y][current_x] == 'o':
                pass
            # skip self-intersections
            elif wire_panel[current_y][current_x] == wire_mark:
                pass
            else:
                wire_panel[current_y][current_x] = 'x'

        current_x += x_factor * 1
        current_y += y_factor * 1
        if wire_panel[current_y][current_x] != 'o':
            wire_panel[current_y][current_x] = '+'

        # print_panel(wire_panel)


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        panels = f.read().splitlines()
    
    # for debugging
    # panels = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
    directions_1 = [ direction for direction in panels[0].split(',')]
    directions_2 = [ direction for direction in panels[1].split(',')]

    wire_panel = [['.' for i in range(30000)] for j in range(20000)]

    start_y = 10000
    start_x = 10000
    wire_panel[start_y][start_x] = 'o'
    
    follow_wire(wire_panel, directions_1, start_x, start_y, '1')
    follow_wire(wire_panel, directions_2, start_x, start_y, '2')
    
    #print_panel(wire_panel)
    
    minimum_distance = 1000000
    for i, row in enumerate(wire_panel):
        for j, col in enumerate(row):
            if col == 'x':
                distance_to_origin = abs(start_y - j) + abs(start_x - i)
                minimum_distance = min([minimum_distance, distance_to_origin])
    print(minimum_distance)


if __name__== "__main__":
  main()
