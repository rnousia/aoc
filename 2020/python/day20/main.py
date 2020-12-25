import os
import re
from functools import reduce

DIRECTIONS = ['north', 'south', 'east', 'west']
OPPOSITES = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}

class TileMosaic():
    def __init__(self, tiles):
        self.tiles = tiles
        self.mosaic = None

    def get_tile_by_id(self, id):
        return [tile for tile in self.tiles if tile.id == id][0]
    
    def create_mosaic(self, id):
        mosaic_data = []
        row_data = []

        tile_at_left_corner = [tile for tile in self.tiles if sorted(tile.neighbours.keys()) == sorted(['south', 'east'])]
        tile_at_left = tile_at_left_corner[0] if len(tile_at_left_corner) > 0 else None

        while tile_at_left:
            left_data = tile_at_left.data_without_borders()
            tile_at_right = tile_at_left.neighbours.get('east', None)

            while tile_at_right:
                row_data = []

                for left_row, right_row in zip(left_data, tile_at_right.data_without_borders()):
                    row_data.append(left_row + right_row)
                
                left_data = row_data.copy()
                tile_at_right = tile_at_right.neighbours.get('east', None)

            tile_at_left = tile_at_left.neighbours.get('south', None)
            mosaic_data.extend(row_data)

        self.mosaic = ImageTile(id, mosaic_data)
    
    def __str__(self):
        result_str = ''

        tile_at_left_corner = [tile for tile in self.tiles if sorted(tile.neighbours.keys()) == sorted(['south', 'east'])]
        tile_at_left = tile_at_left_corner[0] if len(tile_at_left_corner) > 0 else None

        while tile_at_left:
            result_str += str(tile_at_left.id) + '|'
            tile_at_right = tile_at_left.neighbours.get('east', None)

            while tile_at_right:
                result_str += str(tile_at_right.id)
                tile_at_right = tile_at_right.neighbours.get('east', None)

                if tile_at_right:
                    result_str += '|'
                
            result_str += '\n'
            tile_at_left = tile_at_left.neighbours.get('south', None)

        return result_str


class ImageTile():
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.neighbours = {}
        self.borders = {}

        # Init tile borders
        self.update_borders()

    def rotate(self):
        data = [list(row) for row in self.data]
        self.data = [''.join(pixel) for pixel in zip(*data[::-1])]
        self.update_borders()
    
    def flip(self):
        for i, row in enumerate(self.data):
            self.data[i] = row[::-1]
        self.update_borders()
    
    def update_borders(self):
        self.borders['north'] = self.data[0]
        self.borders['east'] = ''.join([col for row in self.data for i, col in enumerate(row) if i == len(row) - 1])
        self.borders['south'] = self.data[-1]
        self.borders['west'] = ''.join([col for row in self.data for i, col in enumerate(row) if i == 0])
    
    def data_without_borders(self):
        return [row[1:-1] for row in self.data[1:-1]]
    
    def borders_match(self, tile):
        matching_directions = []
        for direction in DIRECTIONS:
            if self.borders[direction] == tile.borders[OPPOSITES[direction]]:
                matching_directions.append(direction)
        
        return matching_directions

    def add_neighbour(self, tile):
        match = None
        # Check if new tile matches any borders and nothing is added yet
        for direction in DIRECTIONS:
            if not isinstance(self.borders[direction], ImageTile) \
                and self.borders[direction] == tile.borders[OPPOSITES[direction]]:
                if not isinstance(tile.borders[OPPOSITES[direction]], ImageTile):
                    match = direction
                    self.neighbours[direction] = tile
  
        if not match:
            return False

        directions_to_check = ('north', 'south') if match in ('east', 'west') else ('east', 'west')

        # Update neighbours
        for direction in directions_to_check:
            if direction in self.neighbours:
                # Check if neighbour tile exist
                neighbour_tile = self.neighbours[direction].neighbours.get(match, None)
                if neighbour_tile:
                    # Check if tile border is the same with the neighbour
                    if neighbour_tile.borders[OPPOSITES[direction]] == tile.borders[direction]:
                        neighbour_tile.neighbours[OPPOSITES[direction]] = tile
                        tile.neighbours[direction] = neighbour_tile
                    else:
                        raise ValueError('Tile borders should have matched:',
                            neighbour_tile.borders[OPPOSITES[direction]],
                            tile.borders[direction])
                    # Go further if possible
                    if match in neighbour_tile.neighbours:
                        opposite_tile = neighbour_tile.neighbours[match].neighbours.get(OPPOSITES[direction], None)
                        if opposite_tile:
                            if opposite_tile.borders[OPPOSITES[match]] == tile.borders[match]:
                                opposite_tile.neighbours[OPPOSITES[match]] = tile
                                tile.neighbours[match] = opposite_tile
                            else:
                                raise ValueError('Tile borders should have matched:',
                                opposite_tile.borders[OPPOSITES[direction]],
                                tile.borders[match] )
        return True
        
    def __str__(self):
        return str(self.id) + '\n' + '\n'.join(self.data) + '\n'


def find_matching_tiles(target_tile, tiles):
    matching_tiles = {}
    tiles_matched = []
    for tile in [tile for tile in tiles if tile.id != target_tile.id]:
        match_found = None
        for flip in range(2):
            num_rotations = 0
            while num_rotations < 4:
                match_found = target_tile.borders_match(tile)
                if len(match_found) > 0:
                    for match in match_found:
                        if tile.id not in tiles_matched:
                            tiles_matched.append(tile.id)
                            matching_tiles[tile.id] = match
                        num_rotations = 4
                else:
                    tile.rotate()
                    num_rotations += 1
            if not match_found and flip == 0:
                tile.flip()
    
    return matching_tiles


def find_pattern(pattern, image):
    pattern_index = []
    for row in pattern:
        pattern_index.append([match.start() for match in re.finditer('#', row)])
    
    num_patterns_found = 0
    for i in range(len(image.data) - 3):
        for j in range(len(image.data[0]) - len(pattern[0])):
            matches = 0
            for pattern_row in [1,2,0]:
                for index in pattern_index[pattern_row]:
                    if image.data[i+pattern_row][j+index] == '#':
                        matches += 1
                    else:
                        break
                else:
                    continue
                break
            else:
                if matches == ''.join(pattern).count('#') :
                    num_patterns_found += 1

    return num_patterns_found


def split_list(input_list, separator):
    sub_list = []
    for item in input_list:
        if item == separator:
            yield sub_list
            sub_list = []
        else:
            sub_list.append(item)
    yield sub_list


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        lines = f.read().splitlines()

    # Parse input data
    tile_data = [item for item in split_list(lines, '')]
    tiles = []
    for data in tile_data:
        id = int(data[0].replace('Tile ','').replace(':',''))
        tiles.append(ImageTile(id, data[1:]))
   
    # Find possible neighbours for all tiles
    neighbours = {}
    for tile in tiles:
        neighbours[tile.id] = find_matching_tiles(tile, tiles)

    corner_tiles = [key for key in neighbours.keys() if len(neighbours[key]) == 2]


    # Part 1
    result = reduce((lambda x, y: x * y), corner_tiles)
    print('Part 1 result:', result)
    # 20899048083289
  
    # Part 2
    mosaic = TileMosaic(tiles.copy())
    unoriented_tile_ids = [tile.id for tile in tiles]
    
    # Start assembling from corner tile
    target_tile_id = corner_tiles.pop(0)
    target_tile = mosaic.get_tile_by_id(target_tile_id)
    unoriented_tile_ids.remove(target_tile_id)
    target_tiles = []

    # Add neighbouring tiles to queue
    queue = []
    for tile_id in neighbours[target_tile.id].keys():
        tile = mosaic.get_tile_by_id(tile_id)
        queue.append(tile)
        unoriented_tile_ids.remove(tile_id)
    
    while target_tile:
        # Check tiles in queue
        while len(queue) > 0:

            tile = queue.pop(0)
            neighbour_found = False

            for flip in range(2):

                num_rotations = 0

                while num_rotations < 4:

                    neighbour_found = target_tile.add_neighbour(tile)

                    if neighbour_found:
                        tile.add_neighbour(target_tile)
                        
                        # Add found tile to targets for next round
                        if tile.id not in [tile.id for tile in target_tiles]:
                            target_tiles.append(tile)

                        num_rotations = 4
                    else:
                        tile.rotate()
                        num_rotations += 1
            
                if neighbour_found:
                    pass
            
                elif not neighbour_found and flip == 0:
                    tile.flip()

            if not neighbour_found:
                unoriented_tile_ids.append(tile.id)

        # Choose next target tile
        target_tile = None
        min_neighbours = 5
        for tile in target_tiles:
            if len(tile.neighbours) != len(neighbours[tile.id]):
                
                # Choose the next target based on number of possible neighbours: prefer corners and borders
                if len(neighbours[tile.id]) < min_neighbours:
                    target_tile = tile
                    min_neighbours = len(neighbours[tile.id])
            
            # If number of maximum neighbours is reached, remove tile from targets
            else:
                if tile.id in unoriented_tile_ids:
                    unoriented_tile_ids.remove(tile.id)
        
        if target_tile:
            target_tiles = [tile for tile in target_tiles if tile.id != target_tile.id]

            # Add neighbours of the new target tile to queue  
            queue = []
            for tile_id in neighbours[target_tile.id].keys():
                tile = mosaic.get_tile_by_id(tile_id)
                if tile_id in unoriented_tile_ids:
                    queue.append(tile)
           

    # Mosaic tiles together
    print(mosaic)
    mosaic.create_mosaic(1)
    print(mosaic.mosaic)

    SEA_MONSTER = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]
    
    # Find pattern from mosaic
    for flip in range(2):
        num_rotations = 0
        while num_rotations < 5:
            num_monsters_found = find_pattern(SEA_MONSTER, mosaic.mosaic)
            if num_monsters_found > 0:
                num_rotations = 5
            else:
                mosaic.mosaic.rotate()
                num_rotations += 1
        
        if num_monsters_found > 0:
            break
        else:
            mosaic.mosaic.flip()

    print('Part 2 answer: ', ''.join(mosaic.mosaic.data).count('#') - num_monsters_found * ''.join(SEA_MONSTER).count('#'))
    # 1559


if __name__ == '__main__':
    main()
