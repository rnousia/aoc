'''
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

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
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?
'''
import os


def print_panel(matrix):
    print('\n'.join([''.join([item for item in row]) for row in matrix]))

def calculate_factors(direction):
    x_factor = 0
    y_factor = 0
    if direction == 'R':
        x_factor = 1
    elif direction == 'L':
        x_factor = -1
    elif direction == 'U':
        y_factor = -1
    elif direction == 'D':
        y_factor = 1
    return (x_factor, y_factor)

def follow_wire(wire_panel, directions, start_x, start_y, wire_mark, create_panel=True):
    current_x = start_x
    current_y = start_y

    distance_to_intersection = 0
    intersections = []

    for direction in directions:
        x_factor, y_factor = calculate_factors(direction[0])
        distance = int(direction[1:])

        
        for step in range(distance - 1):
            current_x += x_factor * 1
            current_y += y_factor * 1

            # creates initial matrix with intersections and self-intersection marked
            if create_panel:
                if wire_panel[current_y][current_x] == '.':
                    wire_panel[current_y][current_x] = wire_mark
                elif wire_panel[current_y][current_x] == 'o':
                    pass
                # mark self-intersections
                elif wire_panel[current_y][current_x] == wire_mark:
                    wire_panel[current_y][current_x] = 's'
                # mark intersections
                else:
                    wire_panel[current_y][current_x] = 'x'
            
            # calculate wire distance to intersections
            else:
                distance_to_intersection += 1
                elif wire_panel[current_y][current_x] == 'x':
                    intersections.append({
                        'location': (current_y, current_x),
                        'distance': distance_to_intersection
                    })

        current_x += x_factor * 1
        current_y += y_factor * 1

        # when creating matrix
        if create_panel:
            if wire_panel[current_y][current_x] != 'o':
                wire_panel[current_y][current_x] = '+'
        else:
            distance_to_intersection += 1

        # print_panel(wire_panel)
    return intersections


def main(panels, panel_size):
    directions_1 = [ direction for direction in panels[0].split(',')]
    directions_2 = [ direction for direction in panels[1].split(',')]

    wire_panel = [['.' for i in range(panel_size)] for j in range(panel_size)]

    start_y = int(panel_size / 2)
    start_x = int(panel_size / 2)
    wire_panel[start_y][start_x] = 'o'
    
    # create wire panel
    follow_wire(wire_panel, directions_1, start_x, start_y, '1')
    follow_wire(wire_panel, directions_2, start_x, start_y, '2')

    # calculate distances
    wire1_intersections = follow_wire(wire_panel, directions_1, start_x, start_y, '1', create_panel=False)
    wire2_intersections = follow_wire(wire_panel, directions_2, start_x, start_y, '2', create_panel=False)
    
    #print_panel(wire_panel)
    
    min_distance = 100000000
    for intersection in wire1_intersections:
        #print(intersection)
        distance_sum = intersection['distance'] + [intersection2['distance'] for intersection2 in wire2_intersections if intersection2['location'] == intersection['location']][0]
        min_distance = min([distance_sum, min_distance])
    
    print(min_distance)


if __name__== "__main__":
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        panels = f.read().splitlines()

    panel_size = 28000
    main(panels, panel_size)

    # for debugging
    panels = ['R8,U5,L5,D3', 'U7,R6,D4,L4'] # expected result 30 steps
    main(panels, 50)
    panels = ['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'] # expected result 610 steps
    main(panels, 600)
    panels = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'] # expected result 410 steps
    main(panels, 600)
    # 9320
