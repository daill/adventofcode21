import os
import re
from typing import DefaultDict

def read_input():
    target_area = []
    with open(os.path.abspath("./1217/input")) as file: 
        lines = file.readlines()
        for line in lines:
            m = line.strip("\n")
            g = re.match(r"^.*x=(\d+)\.\.(\d+), y=([-]*\d+)\.\.([-]*\d+)", m)
            x1 = int(g.group(1))
            x2 = int(g.group(2))
            y1 = int(g.group(3))
            y2 = int(g.group(4))
            target_area = [x1, x2, y1, y2]
    return target_area

def trajectory(velocity, target_area):
    x,y = velocity
    coord = [0,0]
    max_y = 0
    while coord[0] < target_area[1] and coord[1] > target_area[2]:
        coord[0] += x
        coord[1] += y
        if x > 0:
            x-=1
        y -= 1
        max_y = max(max_y, coord[1])
        if coord[0] <= target_area[1] and coord[0] >= target_area[0] and coord[1] >= target_area[2] and coord[1] <= target_area[3]:
            print("cx{0} cy{1} v{2} t{3}".format(coord[0],coord[1], velocity, target_area))
            return velocity
    return 0

if __name__ == '__main__':
    results = []
    target_area = read_input()
    for x in range(1,(target_area[1]+1)):
        for y in range(0, abs(target_area[2])+1):
            v = trajectory((x,y), target_area)
            if v != 0:
                if v not in results:
                    results.append(v)
            v = trajectory((x,-y), target_area)
            if v != 0:
                if v not in results:
                    results.append(v)
    print("{0}".format(len(results)))