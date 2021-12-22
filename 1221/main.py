from collections import defaultdict
import os
from itertools import product


def read_input():
    players = []
    positions = []
    with open(os.path.abspath("./1221/input")) as file: 
        f = file.read().split('\n')
        for y in range(len(f)):
            line = list(f[y].strip('\n').split(" "))
            players.append(line[2])
            positions.append(int(line[-1]))
    return players, positions

# part one
def det_dice(start):
    res = start+(start+1)+(start+2)
    return res

def process_1(positions):
    scores = positions.copy()
    first = []
    dice = 1
    while True:
        for i in range(len(players)):            
            res = det_dice(dice)
            dice+=3
            pos = (positions[i]+res)%10
            pos = pos if pos != 0 else 10

            if i not in first:
                first.append(i)
                scores[i] = pos
                positions[i] = pos
            else:
                positions[i] = pos
                scores[i] += pos
            if max(scores) >= 21:
                return scores, positions, dice

def process_2(positions):
    scores = positions.copy()
    first = []
    dice = 1
    while True:
        for i in range(len(players)):            
            res = det_dice(dice)
            dice+=3
            pos = (positions[i]+res)%10
            pos = pos if pos != 0 else 10

            if i not in first:
                first.append(i)
                scores[i] = pos
                positions[i] = pos
            else:
                positions[i] = pos
                scores[i] += pos
            if max(scores) >= 21:
                return scores, positions, dice


def process_2(positions):
    rolls = tuple(map(sum, product(range(1, 4), range(1, 4), range(1, 4))))

    universes = []
    for i in range(len(positions)):
        universes.append([(i, positions[i], 0)])

    wins = [0,0]

    while True:
        for idx, universe in enumerate(universes):
            t_universe = []
            for uv in universe:
                player, position, score = uv
                for j in rolls:
                    t_pos = position
                    t_score = score

                    pos = (t_pos+j)%10
                    pos = pos if pos != 0 else 10
                
                    t_pos = pos
                    t_score += pos
                    uni = (player, t_pos, t_score)

                    if t_score >= 21:
                        wins[idx] += 1
                    else:
                        t_universe.append(uni)
                        
            universes[idx] = t_universe
                

if __name__ == '__main__':
    players, positions = read_input()
    #scores, positions, dice = process_1(positions)
    #scores.sort()
    #loser = scores[0]
    #print("val {0}".format(loser*(dice-1)))
    rolls = tuple(map(sum, product(range(1, 4), range(1, 4), range(1, 4))))
    process_2(positions)
    
    pass