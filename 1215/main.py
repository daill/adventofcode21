import os
from typing import DefaultDict
import sys

def read_input():
    map = DefaultDict()
    with open(os.path.abspath("./1215/input")) as file: 
        lines = file.readlines()
        for i, line in enumerate(lines):
            map[i] = list(line.strip())
    return map

def find_way(cavemap, mult):
    seen = [(0, 0)]
    queue = [(0, 0, 0)]
    while len(queue) > 0:
        queue.sort()
        dist, x, y = queue.pop(0)
        if x == mult*len(cavemap)-1 and y == mult*len(cavemap[0])-1:
            return dist

        for dx, dy in ((0,1), (1,0), (-1,0), (0, -1)):
            n_x, n_y = x+dx, y+dy

            if n_x < 0 or n_y < 0 or n_x >= mult*len(cavemap) or n_y >= mult*len(cavemap[0]):
                continue
            
            nn_x = n_x % len(cavemap)
            nn_y = n_y % len(cavemap[0])
            d = int(cavemap[nn_y][nn_x])
            n_d = (d + (n_y // (len(cavemap)) + (n_x // (len(cavemap[0]))))-1) % 9 +1

            if (n_x, n_y) not in seen:
                seen.append((n_x, n_y))
                queue.append((dist + n_d, n_x, n_y))

if __name__ == '__main__':
    cavemap = read_input()

    print(find_way(cavemap, 5))


