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
from collections import Counter

def read_input():
    with open(os.path.abspath("./1205/input")) as file: 
        lines = file.readlines()

        movements = list()
        for line in lines:
            splited = line.split(" ")
            first = splited[0].split(",")
            second = splited[2].split(",")
            movements.append([int(first[0]), int(first[1]), splited[1], int(second[0]), int(second[1])])
        #movements.append([int(first[0]), int(first[1]), splited[1], int(second[0]), int(second[1])])
        #print("movements {0}".format(movements))
    return movements

def process_movements_laterals(movements):
    maxX = 0
    maxY = 0
    laterals = []
    for movement in movements:
        x = max(movement[0], movement[3])
        y = max(movement[1], movement[4])
        if maxX < x:
            maxX = x
        if maxY < y:
            maxY = y
        if ((movement[0] == movement[3]) or (movement[1] == movement[4])):
            laterals.append(movement)
    locMap = [[0] * (maxX+1) for i in range((maxY+1))]
    #del laterals[326]
    for lateral in laterals:
        if lateral[0] == lateral[3]:
            xCord = lateral[0]
            for yCord in range(min(lateral[1], lateral[4]), max(lateral[1], lateral[4])+1):
                locMap[yCord][xCord] += 1
                #print("x {0} -> {1}".format(xCord, yCord))
        if lateral[1] == lateral[4]:
            yCord = lateral[1]
            for xCord in range(min(lateral[0], lateral[3]), max(lateral[0], lateral[3])+1):
                locMap[yCord][xCord] += 1
                #print("y {0} -> {1}".format(xCord, yCord))

    return locMap

def process_movements_diagonals(movements):
    maxX = 0
    maxY = 0
    laterals = []
    for movement in movements:
        x = max(movement[0], movement[3])
        y = max(movement[1], movement[4])
        if maxX < x:
            maxX = x
        if maxY < y:
            maxY = y
        if ((movement[0] == movement[3]) 
            or (movement[1] == movement[4]) 
            or (movement[0] == movement[1] and movement[3] == movement[4])
            or (abs(movement[4]-movement[1]) == abs(movement[0]-movement[3]))):
            laterals.append(movement)
        

    locMap = [[0] * (maxX+1) for i in range((maxY+1))]

    for lateral in laterals:
        if lateral[0] == lateral[3]:
            xCord = lateral[0]
            for yCord in range(min(lateral[1], lateral[4]), max(lateral[1], lateral[4])+1):
                locMap[yCord][xCord] += 1
                #print("x {0} -> {1}".format(xCord, yCord))
        if lateral[1] == lateral[4]:
            yCord = lateral[1]
            for xCord in range(min(lateral[0], lateral[3]), max(lateral[0], lateral[3])+1):
                locMap[yCord][xCord] += 1
                #print("y {0} -> {1}".format(xCord, yCord))

        if (lateral[0] == lateral[1] and lateral[3] == lateral[4]) or (abs(lateral[4]-lateral[1]) == abs(lateral[0]-lateral[3])):
            x1 = lateral[0]
            y1 = lateral[1]
            x2 = lateral[3]
            y2 = lateral[4]
            xCord = x1
            yCord = y1
            while xCord != x2 and yCord != y2:
                locMap[yCord][xCord] += 1
                if (xCord >= x2):
                    xCord -= 1
                else:
                    xCord += 1
                if (yCord >= y2):
                    yCord -= 1
                else:
                    yCord += 1
            locMap[yCord][xCord] += 1

          
    return locMap

def calc_oc(locMap):
    cnt = 0
    for i, line in enumerate(locMap):
        cnt += len(list(filter(lambda x: x >=2 and x <=5, line)))
    return cnt

if __name__ == '__main__':
    movements = read_input()
    # part one
    locMap = process_movements_laterals(movements)
    value = calc_oc(locMap)
    print("value {0}".format(value))
    # part two
    locMap = process_movements_diagonals(movements)
    value = calc_oc(locMap)
    print("value {0}".format(value))