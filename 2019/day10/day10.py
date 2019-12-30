'''
You fly into the asteroid belt and reach the Ceres monitoring station. The Elves here have an emergency: they're having trouble tracking all of the asteroids and can't be sure they're safe.

The Elves would like to build a new monitoring station in a nearby area of space; they hand you a map of all of the asteroids in that region (your puzzle input).

The map indicates whether each position is empty (.) or contains an asteroid (#). The asteroids are much smaller than they appear on the map, and every asteroid is exactly in the center of its marked position. The asteroids can be described with X,Y coordinates where X is the distance from the left edge and Y is the distance from the top edge (so the top-left corner is 0,0 and the position immediately to its right is 1,0).

Your job is to figure out which asteroid would be the best place to build a new monitoring station. A monitoring station can detect any asteroid to which it has direct line of sight - that is, there cannot be another asteroid exactly between them. This line of sight can be at any angle, not just lines aligned to the grid or diagonally. The best location is the asteroid that can detect the largest number of other asteroids.

For example, consider the following map:

.#..#
.....
#####
....#
...##
The best location for a new monitoring station on this map is the highlighted asteroid at 3,4 because it can detect 8 asteroids, more than any other location. (The only asteroid it cannot detect is the one at 1,0; its view of this asteroid is blocked by the asteroid at 2,2.) All other asteroids are worse locations; they can detect 7 or fewer other asteroids. Here is the number of other asteroids a monitoring station on each asteroid could detect:

.7..7
.....
67775
....7
...87
Here is an asteroid (#) and some examples of the ways its line of sight might be blocked. If there were another asteroid at the location of a capital letter, the locations marked with the corresponding lowercase letter would be blocked and could not be detected:

#.........
...A......
...B..a...
.EDCG....a
..F.c.b...
.....c....
..efd.c.gb
.......c..
....f...c.
...e..d..c
Here are some larger examples:

Best is 5,8 with 33 other asteroids detected:

......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
Best is 1,2 with 35 other asteroids detected:

#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
Best is 6,3 with 41 other asteroids detected:

.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
Best is 11,13 with 210 other asteroids detected:

.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
Find the best location for a new monitoring station. How many other asteroids can be detected from that location?

Your puzzle answer was 326.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Once you give them the coordinates, the Elves quickly deploy an Instant Monitoring Station to the location and discover the worst: there are simply too many asteroids.

The only solution is complete vaporization by giant laser.

Fortunately, in addition to an asteroid scanner, the new monitoring station also comes equipped with a giant rotating laser perfect for vaporizing asteroids. The laser starts by pointing up and always rotates clockwise, vaporizing any asteroid it hits.

If multiple asteroids are exactly in line with the station, the laser only has enough power to vaporize one of them before continuing its rotation. In other words, the same asteroids that can be detected can be vaporized, but if vaporizing one asteroid makes another one detectable, the newly-detected asteroid won't be vaporized until the laser has returned to the same position by rotating a full 360 degrees.

For example, consider the following map, where the asteroid with the new monitoring station (and laser) is marked X:

.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##
The first nine asteroids to get vaporized, in order, would be:

.#....###24...#..
##...##.13#67..9#
##...#...5.8####.
..#.....X...###..
..#.#.....#....##
Note that some asteroids (the ones behind the asteroids marked 1, 5, and 7) won't have a chance to be vaporized until the next full rotation. The laser continues rotating; the next nine to be vaporized are:

.#....###.....#..
##...##...#.....#
##...#......1234.
..#.....X...5##..
..#.9.....8....76
The next nine to be vaporized are then:

.8....###.....#..
56...9#...#.....#
34...7...........
..2.....X....##..
..1..............
Finally, the laser completes its first full rotation (1 through 3), a second rotation (4 through 8), and vaporizes the last asteroid (9) partway through its third rotation:

......234.....6..
......1...5.....7
.................
........X....89..
.................
In the large example above (the one with the best monitoring station location at 11,13):

The 1st asteroid to be vaporized is at 11,12.
The 2nd asteroid to be vaporized is at 12,1.
The 3rd asteroid to be vaporized is at 12,2.
The 10th asteroid to be vaporized is at 12,8.
The 20th asteroid to be vaporized is at 16,0.
The 50th asteroid to be vaporized is at 16,9.
The 100th asteroid to be vaporized is at 10,16.
The 199th asteroid to be vaporized is at 9,6.
The 200th asteroid to be vaporized is at 8,2.
The 201st asteroid to be vaporized is at 10,9.
The 299th and final asteroid to be vaporized is at 11,1.
The Elves are placing bets on which will be the 200th asteroid to be vaporized. Win the bet by determining which asteroid that will be; what do you get if you multiply its X coordinate by 100 and then add its Y coordinate? (For example, 8,2 becomes 802.)
'''
import os
from copy import deepcopy
from math import sqrt, atan2, degrees


class Asteroid:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.angle = None


def check_if_between(origin, point1, point2):
    # Points align if cross product of vectors is 0
    cross_product = (point2.y - origin.y) * (point1.x - origin.x) - (point2.x - origin.x) * (point1.y - origin.y)
    if cross_product == 0:
        # Point2 is between origin and point1,
        # if dot product of vectors is positive and
        # less than the square of the length of vector1.
        dot_product = (point2.x - origin.x) * (point1.x - origin.x) + (point2.y - origin.y)*(point1.y - origin.y)
        squared_vector1_length = (point1.x - origin.x) * (point1.x - origin.x) + (point1.y - origin.y) * (point1.y - origin.y)

        if dot_product > 0.0 and dot_product < squared_vector1_length:
            # Return distance for Part 2 calculation
            return sqrt(squared_vector1_length)
    
    return -1


def count_max_direct_line_of_sights(asteroids):
    max_direct_lines = 0
    asteroid_id = None
    for origin_asteroid in asteroids:
        direct_line_of_sights = 0
        for asteroid1 in [x for x in asteroids if x.id != origin_asteroid.id]:
            free_line_of_sight = True
            
            for asteroid2 in [x for x in asteroids if x.id != origin_asteroid.id and x.id != asteroid1.id]:
                if check_if_between(origin_asteroid, asteroid1, asteroid2) > 0:
                    free_line_of_sight = False
            if free_line_of_sight:
                direct_line_of_sights += 1
        
        if max_direct_lines < direct_line_of_sights:
            max_direct_lines = direct_line_of_sights
            asteroid_id = origin_asteroid.id
    
    return max_direct_lines, asteroid_id


def use_laser(laser_base, all_asteroids):
    asteroids = deepcopy(all_asteroids)

    laser_target = Asteroid(None, laser_base.x, 0)
    laser_target.angle = 0

    # Remove the station asteroid from asteroids list
    asteroids.pop(laser_base.id)
    asteroids_count = len(asteroids)

    # Calculate angle to laser for all asteroids (0 - 360 degrees)
    laser_direction = atan2(laser_target.y - laser_base.y, laser_target.x - laser_base.x)
    for asteroid in asteroids:
        asteroid_direction = atan2(asteroid.y - laser_base.y, asteroid.x - laser_base.x)
        asteroid.angle = degrees(laser_direction - asteroid_direction) % 360

    asteroids.sort(key=lambda x: x.angle )

    while asteroids_count - len(asteroids) < 200:
        asteroid_id_to_destroy = None
        min_distance = None

        target_asteroids = [asteroid for asteroid in asteroids if asteroid.angle == laser_target.angle]

        if len(target_asteroids) > 1:
            # If multiple asteroids are aligned, destory the closest one
            for asteroid in target_asteroids:
                distance = check_if_between(laser_base, laser_target, asteroid)
                min_distance = min(min_distance, distance) if asteroid_id_to_destroy else distance
                asteroid_id_to_destroy = asteroid.id
        elif len(target_asteroids) == 1:
            asteroid_id_to_destroy = target_asteroids[0].id
        
        if asteroid_id_to_destroy is not None:
            asteroids.pop([index for index, a in enumerate(asteroids) if a.id == asteroid_id_to_destroy][0])
            # Stop if no asteroid is left
            if len(asteroids) == 0:
                break
        
        # Move laser to next asteroid
        if asteroids[-1].angle <= laser_target.angle:
            laser_target = asteroids[0]
        else:
            for asteroid in asteroids:
                if asteroid.angle > laser_target.angle:
                    laser_target = asteroid
                    break


    return asteroid_id_to_destroy


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        input = f.read().split('\n')

    asteroids = []
    asteroid_id = 0
    for y, row in enumerate(input):
        for x, col in enumerate(row):
            if col == '#':
                asteroids.append(Asteroid(asteroid_id, x, 0 - y))
                asteroid_id += 1

    # Part 1
    max_direct_lines, station_asteroid_id = count_max_direct_line_of_sights(asteroids)
    print(max_direct_lines, station_asteroid_id, [(a.x, a.y) for a in asteroids if a.id == station_asteroid_id])

    # Part 2
    last_destroyed_id = use_laser(asteroids[354], asteroids)
    print(asteroids[last_destroyed_id].x * 100 + (asteroids[last_destroyed_id].y * -1))

    


  
if __name__== '__main__':
  main()