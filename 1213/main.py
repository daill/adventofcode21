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


from posixpath import splitext
from typing import Tuple
import re
import os


def read_input():
    lines = []
    sheet = list()
    coords = []
    folds = []
    with open(os.path.abspath("./1213/input")) as file: 
        lines = file.readlines()
        size_y = 0
        size_x = 0
        fold_x = 0
        fold_y = 0
        
        for line in lines:
            if "," in line:
                splitted = line.strip().split(",")
                size_x = max(int(splitted[0]), size_x)
                size_y = max(int(splitted[1]), size_y)
                coords.append((int(splitted[0]), int(splitted[1])))
            if "=" in line:
                m = re.search('^fold along (\w)=(\d*)$', line.rstrip())
                folds.append((m.group(1), int(m.group(2))))    
        
        for i in range(size_y+1):
            sheet.append(['.'] * (size_x+1))
    return coords, sheet, folds

def mark(coords, sheet):
    for t1, t2 in coords:
        sheet[t2][t1] = '#'

def fold_x(sheet, fold):
    res = []
    cnt = 0
    for i in range(len(sheet)):
        line_a = sheet[i][:fold]
        line_b = sheet[i][fold+1:]
        line_a.reverse()
        
        for j in range(len(line_b)):
            if line_b[j] == '#':
                line_a[j] = '#'
    
        res.append(line_a)
        cnt += line_a.count('#')
    print("count {0}".format(cnt))
    return res

def fold_y(sheet, fold):
    part_a = sheet[:fold]
    part_b = sheet[fold+1:]
    part_a.reverse()

    res = 0
    for i in range(len(part_b)):
        for j in range(len(part_b[i])):
            if part_b[i][j] == '#':
                part_a[i][j] = '#'
        res += part_a[i].count('#')
    print("count {0}".format(res))
    return part_a


if __name__ == '__main__':
    coords, sheet, folds = read_input()
    mark(coords, sheet)
    for axis, val in folds:
        if axis == 'x':
            sheet = fold_x(sheet, val)
        if axis == 'y':
            sheet = fold_y(sheet, val)
    for line in sheet:
        print(line)
