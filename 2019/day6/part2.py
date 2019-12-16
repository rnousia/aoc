'''
Now, you just need to figure out how many orbital transfers you (YOU) need to take to get to Santa (SAN).

You start at the object YOU are orbiting; your destination is the object SAN is orbiting. An orbital transfer lets you move from any object to an object orbiting or orbited by that object.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
Visually, the above map of orbits looks like this:

                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
In this example, YOU are in orbit around K, and SAN is in orbit around I. To move from K to I, a minimum of 4 orbital transfers are required:

K to J
J to E
E to D
D to I
Afterward, the map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)
'''
import os
from collections import defaultdict


class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


def add_to_tree(parent, child, root):
    if root.children:
        for node in root.children:
            if node.name == parent:
                node.add_child(Node(child))
                return
            else:
                add_to_tree(parent, child, node)
    else:
        if root.name == parent:
            root.add_child(Node(child))


def count_number_of_jumps(path1, path2):
    common_path = list(set(path1).union(set(path2)) - set(path1).intersection(set(path2)))
    return len(common_path)


def track_orbits(root, target, jumps = []):
    if root.children:
        for node in root.children:
            if node.name == target:
                return True
            if node.children:
                if track_orbits(node, target, jumps):
                    jumps.append(node.name)
            if set([x.name for x in node.children]).intersection(set(jumps)):
                jumps.append(node.name)
    return False


def build_orbit_tree(orbits):
    # set COM as root
    orbit_tree = Node('COM')
    # build tree from data
    print('Building tree...')
    parents = ['COM']

    while len(orbits) > 0:
        objects_with_parent = [x for x in orbits if x.split(')')[0] in parents]

        for orbit in objects_with_parent:
            obj, orbiting_obj = orbit.split(')')
            add_to_tree(obj, orbiting_obj, orbit_tree)
            parents.append(orbiting_obj)
            orbits.remove(orbit)
    
    return orbit_tree


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        orbits = f.read().splitlines() 

    # For debugging
    # Given test case:
    # orbits = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L'] # expected count = 42
    # Test case with unordered nodes:
    # orbits = ['C)D', 'D)E', 'E)F', 'COM)B', 'B)C', 'K)L', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K'] # expected count = 42

    orbit_tree = build_orbit_tree(orbits)

    jumps_to_santa = []
    track_orbits(orbit_tree, 'SAN', jumps_to_santa)

    jumps_to_you = []
    track_orbits(orbit_tree, 'YOU', jumps_to_you)

    print(count_number_of_jumps(jumps_to_santa, jumps_to_you))

if __name__== "__main__":
  main()
