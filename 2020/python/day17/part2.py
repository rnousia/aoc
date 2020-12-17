import os

CUBE_STATES = {'active': '#', 'inactive': '.'}

class PocketDimension():
    def __init__(self, initial_state):
        self.cubes = []
        self.cycle = 0

        for y, items in enumerate(initial_state):
            for x, state in enumerate(items):
                self.add_cube(state, (x,y,0,0))
        
        self.update_neighbours()
    
    def next_cycle(self):
        self.cycle += 1
        min_coords, max_coords = self.get_dimensions()

        for z in range(min_coords[0]-1, max_coords[0]+2):
            for y in range(min_coords[1]-1, max_coords[1]+2):
                for x in range(min_coords[2]-1, max_coords[2]+2):
                    for w in range(min_coords[3]-1, max_coords[3]+2):
                        if '{0}_{1}_{2}_{3}'.format(x,y,z,w) not in [cube.id for cube in self.cubes]:
                            self.add_cube(CUBE_STATES['inactive'], (x,y,z,w))
            
        self.update_neighbours()
        
        for cube in self.cubes:
            cube.update_state()

    
    def get_dimensions(self):
        z_values = set([cube.z for cube in self.cubes if is_active(cube.state)])
        y_values = set([cube.y for cube in self.cubes if is_active(cube.state)])
        x_values = set([cube.x for cube in self.cubes if is_active(cube.state)])
        w_values = set([cube.w for cube in self.cubes if is_active(cube.state)])

        return ([min(z_values), min(y_values), min(x_values),  min(w_values)],
            [max(z_values), max(y_values), max(x_values), max(w_values)])

    def __str__(self):
        view = ''
        z_values = sorted(set([cube.z for cube in self.cubes]))
        y_values = sorted(set([cube.y for cube in self.cubes]))
        x_values = sorted(set([cube.x for cube in self.cubes]))
        for z in z_values:
            view += 'z={0}\n'.format(z)
            for y in y_values:
                for x in x_values:
                    view += [cube.state for cube in self.cubes if cube.z == z and cube.y == y and cube.x == x][0]
                view += '\n'
            view += '\n'
        return view
    
    def add_cube(self, state, coordinates):        
        self.cubes.append(Cube(state, coordinates))
    
    def update_neighbours(self):
        for cube in self.cubes:
            if len(cube.neighbours) < 80:
                cube.add_neighbours(self.get_neighbours(cube))
            else:
                cube.update_neighbour_states()

    def get_neighbours(self, center_cube):
        neighbours = center_cube.neighbours.copy()
        neighbour_ids = [cube.id for cube in neighbours]
        for cube in [cube for cube in self.cubes if cube.id != center_cube.id and cube.id not in neighbour_ids]:
            if abs(cube.x - center_cube.x) < 2 and \
                 abs(cube.y - center_cube.y) < 2 and  \
                    abs(cube.z - center_cube.z) < 2 and \
                        abs(cube.w - center_cube.w) < 2:
               
                neighbours.append(cube)
        
        return neighbours

class Cube():
    def __init__(self, state, coordinates):
        self.id = '_'.join([str(coord) for coord in coordinates])
        self.state = state
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        self.w = coordinates[3]
        self.neighbours = []
        self.active_neighbours = []
    
    def add_neighbours(self, neighbours):
        self.neighbours = neighbours
        self.active_neighbours = count_active_cubes(neighbours)
    
    def update_neighbour_states(self):
        self.active_neighbours = count_active_cubes(self.neighbours)

    def update_state(self):
        if is_active(self.state) and not self.active_neighbours in (2,3):
            self.state = CUBE_STATES['inactive']
        elif not is_active(self.state) and self.active_neighbours == 3:
            self.state = CUBE_STATES['active']


def is_active(cube_state):
    return True if cube_state == CUBE_STATES['active'] else False


def count_active_cubes(cubes):
    return [cube.state for cube in cubes].count(CUBE_STATES['active'])



def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        initial_state = f.read().splitlines()

    pocket_dimension = PocketDimension(initial_state)

    while pocket_dimension.cycle < 6:
        pocket_dimension.next_cycle()
        print('Cycle:', pocket_dimension.cycle)

    print('Part 2 answer: ', count_active_cubes(pocket_dimension.cubes))
    # 1836


if __name__ == '__main__':
    main()
