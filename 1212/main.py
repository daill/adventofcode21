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
from collections import defaultdict


def read_input():
    lines = []
    coords = defaultdict(list)
    with open(os.path.abspath("./1212/input")) as file: 
        lines = file.readlines()
        for line in lines:
            splitted = line.strip().split("-")
            coords[splitted[0]] += [splitted[1]]
            coords[splitted[1]] += [splitted[0]]
    return coords


def iterate(coords, way, seen, node, paths, twice):  
    way.append(node)
    if node == "end":
        paths.append(way)
        
    for c in coords[node]:
        if c.islower():
            if c == "start":
                continue
            if c not in seen:
                seen.append(c)
                iterate(coords, way.copy(), seen, c, paths, twice)
            elif twice and c != "end":
                seen.append(c)
                iterate(coords, way.copy(), seen, c, paths, False)
            else:
                continue
        else:
            iterate(coords, way.copy(), seen, c, paths, twice)            
        if c.islower():
            seen.pop()
    
        

def find_ways(coords):
    way = list()
    seen = list()
    paths = list()
    iterate(coords, way, seen, "start", paths, True)
    return paths

if __name__ == '__main__':
    coords = read_input()
    print(len(find_ways(coords)))