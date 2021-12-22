'''
Copyright 2021 Christian Kramer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

## inspired by https://github.com/fuglede/adventofcode/blob/master/2021/day19/solutions.py 


from collections import defaultdict
import os
import re
import numpy as np
from itertools import permutations, product, combinations
import math



def read_input():
    scanners = {}
    rotations = [[]]
    p = re.compile("--- scanner (\d*) ---")
    with open(os.path.abspath("./1219/input")) as file: 
        lines = file.readlines()
        scanner = 0
        for line in lines:
            if line != '\n':
                m = p.search(line.strip('\n'))
                
                if m is not None:
                    scanner = m.group(1)
                    scanners[scanner] = []
                else:
                    split = line.strip('\n').split(',')
                    scanners[scanner].append(np.array([split[0], split[1], split[2]], dtype=int))

    all_rotations = calc_rotations()
    return scanners, all_rotations

def calc_rotations():
    rotations = []
    for x, y, z in permutations([0, 1, 2], 3):
        for sx, sy, sz in product([-1, 1], repeat=3):
            rotation_matrix = np.zeros((3, 3), dtype=int)
            rotation_matrix[0, x] = int(sx)
            rotation_matrix[1, y] = int(sy)
            rotation_matrix[2, z] = int(sz)
            if np.linalg.det(rotation_matrix) > 0:
                rotations.append(rotation_matrix)

    return rotations

def find_beacons(scanner1, scanner2, rotations):
    counter = defaultdict(int)
    for rotation in rotations:
        for beacon1 in scanner1:
            for beacon2 in scanner2:
                result = tuple(beacon1-beacon2 @ rotation)
                counter[result] += 1
                if counter[result] >= 12:
                    # if 12 overlaps return all beacons of scanner j translated to i
                    return counter, result+scanner2 @ rotation, result
    return counter, None, None

def dist(positions):
    print(positions)
    max_dist = 0
    for pos1, pos2 in combinations(positions,2):
        p1x, p1y, p1z = pos1
        p2x, p2y, p2z = pos2
        pos_sum = abs(p1x-p2x)+abs(p1y-p2y)+abs(p1z-p2z)
        max_dist = max(max_dist, pos_sum)
    return max_dist

if __name__ == '__main__':
    scanners, rotations = read_input()
    counter = None
    beacons = set()
    processed = []
    connected = ['0']
    scanner_positions = []
    while connected:
        i = connected.pop()
        for j in scanners.keys():
            if j not in processed and j != i:
                counter, translated_beacons, result = find_beacons(scanners[i], scanners[j], rotations)
                if translated_beacons is not None:
                    print("{0} {1} {2} {3}".format(i,j, processed, connected))   
                    scanners[j] = translated_beacons
                    scanner_positions.append(result)
                    connected.append(j)
        processed.append(i)





    for key in scanners.keys():
        for beacon in scanners[key]:
            beacons.add(tuple(beacon))

    print(len(beacons))
    print(dist(scanner_positions))
    pass
    