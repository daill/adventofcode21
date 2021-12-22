import os
from functools import reduce
from itertools import product
from math import prod
from ast import literal_eval
    

def read_input():
    fishes = []
    with open(os.path.abspath("./1218/input")) as file: 
        lines = file.readlines()
        for line in lines:
            
            depths = []
            values = []
            parse_fish(0, line.strip('\n'), depths, values)
            fishes.append([depths, values])
    
    return fishes

def parse_fish(s, fish, dephts, values, depth=0):    
    while True:
        if s >= len(fish):
            break
        c = fish[s]
        if c == '[':
            depth+=1
        elif c == ']':
            depth-=1
        elif c.isdigit():
            dephts.append(depth)
            values.append(int(c))
        s += 1

def add_fishes(fish1, fish2):
    depths = fish1[0] + fish2[0]
    depths = [x+1 for x in depths]
    values = fish1[1] + fish2[1]
    return [depths, values]

def split(fish):
    idx = None
    for i in range(len(fish[1])):        
        if fish[1][i] > 9:
            idx = i
            break

    if idx is not None:
        val = fish[1][idx]
        fish[0][idx] += 1
        fish[0].insert(idx+1, fish[0][idx])
        fish[1][idx] = val//2
        fish[1].insert(idx+1, val-fish[1][idx])
        return False, fish
    else:
        return True, fish
    

def explode(fish):
    if 5 not in fish[0]:
        return False, fish
    i = fish[0].index(5)
    if i > 0:
        fish[1][i-1] += fish[1][i]
    if i < (len(fish[1])-2):
        fish[1][i+2] += fish[1][i+1]
    fish[1][i+1] = 0
    fish[0][i+1] = 4
    fish[1].pop(i)
    fish[0].pop(i)
    return True, fish

def magnitude(fish):
    f = fish
    while len(f[0]) > 1:
        i = f[0].index(max(f[0]))
        f[1][i+1] = 3 * f[1][i] + 2 * f[1][i+1]
        f[0][i+1] -= 1
        f[1].pop(i)
        f[0].pop(i)
    return f[1][0]

if __name__ == '__main__':
    fishes = read_input()
    
    val = 0
    seen = []
    for i in range(1,len(fishes)):
        for j in range(1,len(fishes)):
            res_fish = fishes[i].copy()
            a = (i,j)
            if a not in seen and i != j:
                res_fish = add_fishes(res_fish, fishes[j].copy())
                while True:
                    #print(res_fish)
                    test, res_fish = explode(res_fish)
                    if test:
                        continue
                    test, res_fish = split(res_fish)
                    if test:
                        break
                val = max(val, magnitude(res_fish))
                print(val)
            seen.append((i,j))
    print(val)