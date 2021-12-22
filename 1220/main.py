from collections import defaultdict
import os

def read_input():
    lights = set()
    algo = []
    with open(os.path.abspath("./1220/input")) as file: 
        f = file.read().split('\n')
        algo = f[0]
        for y in range(2, len(f)):
            line = list(f[y].strip('\n'))
            for x in range(len(line)):
                if line[x] == '#':
                    lights.add((x,y-2))
    return lights, algo


def process_enc(lights, algo, overflow):
    max_l = 0
    min_l = 0
    max_h = 0
    min_h = 0
    newpixels = set()

    for c in lights:
        x,y = c
        max_l = max(max_l, x)
        min_l = min(min_l, x)
        max_h = max(max_h, y)
        min_h = min(min_h, y)

    for y in range(min_h-2, max_h+2):
        for x in range(min_l-2, max_l+2):
            seq = 0
            for i in range(3):
                for j in range(3):
                    seq <<= 1
                    seq |= ((x+j, y+i) in lights)
                    seq |= overflow and ((y+i) < min_h or (y+i) > max_h or (x+j) < min_l or (x+j) > max_l)
            if algo[seq] == '#':
                newpixels.add((x+1,y+1))
    return newpixels

if __name__ == '__main__':
    lights, algo = read_input()
    for i in range(50):
        lights = process_enc(lights, algo, i%2!=0)
    print(len(lights))

