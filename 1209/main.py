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


import os

def read_input():
    heightmap = list()
    width = 0
    with open(os.path.abspath("./1209/input")) as file: 
        lines = file.readlines()
        for line in lines:
            line = line.strip('\n').strip(' ')
            width = len(line)
            heightmap.extend(line.strip('\n'))
    return heightmap, width, len(lines)

# part one
def find_local_min(heightmap, width):
    mid, up, down, left, right = 0, 0, 0, 0, 0
    minima = list()
    basins = list()

    for i in range(len(heightmap)):
        mid = int(heightmap[i])
        norm = i%width
        if i < width:
            up = -1
        else: 
            up = int(heightmap[i-width])
        
        if i+width >= len(heightmap):
            down = -1
        else: 
            down = int(heightmap[i+width])

        if norm+1 > width:
            right = -1
        else:
            if i+1 >= len(heightmap):
                right = -1
            else: 
                right = int(heightmap[i+1])

        if norm-1 < 0:
            left = -1
        else:
            left = int(heightmap[i-1])
        
        if up != -1:
            if up <= mid:
                continue
        if down != -1:
            if down <= mid:
                continue
        if right != -1:
            if right <= mid:
                continue
        if left != -1: 
            if left <= mid:
                continue

        print("min found {0}, up {1}, down {2}, left {3}, right {4} x {5},y {6}".format(mid, up, down, left, right, i/width, i%width))
        minima.append(mid)
        basin = walk(heightmap, i, [], width)
        print("basin of {0} size {1}".format(mid, len(basin)))
        basins.append(len(basin))

    return minima, basins

# part two
def walk(heightmap, index, used_ids, width):
    up, down, left, right = 0, 0, 0, 0
    norm = index%width

    if index < width:
        up = -1
    else: 
        up = int(heightmap[index-width])
    
    if index+width >= len(heightmap):
        down = -1
    else: 
        down = int(heightmap[index+width])

    if norm+1 >= width:
        right = -1
    else:
        if index+1 >= len(heightmap):
            right = -1
        else: 
            right = int(heightmap[index+1])

    if norm-1 < 0:
        left = -1
    else:
        left = int(heightmap[index-1])
    
    used_ids.append(index)
    if up != -1:
        if up < 9 and index-width not in used_ids:
            used_ids = walk(heightmap, index-width, used_ids, width)
    if down != -1:
        if down < 9 and index+width not in used_ids:
            used_ids = walk(heightmap, index+width, used_ids, width)
    if right != -1:
        if right < 9 and index+1 not in used_ids:
            used_ids = walk(heightmap, index+1, used_ids, width)
    if left != -1: 
        if left < 9 and index-1 not in used_ids:
             used_ids = walk(heightmap, index-1, used_ids, width)
    return used_ids

def sum_up(minima):
    res = 0
    for num in minima:
        res += 1+num
    return res

if __name__ == '__main__':
    heightmap, width, height = read_input()
    minima, basins = find_local_min(heightmap, width)
    print("sum {0}".format(sum_up(minima)))
    basins.sort(reverse=True)
    product = basins[0] * basins[1] * basins[2]
    print("{0}".format(product))