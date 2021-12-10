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

OPENINGS = "<([{"
ENDINGS = ">)]}"

def read_input():
    lines = []
    with open(os.path.abspath("./1210/input")) as file: 
        lines = file.readlines()
    return lines

def parse_lines(lines):
    sum1 = 0
    sum2 = []
    sum3 = 0
    for line in lines:
        print("line {0} -----".format(line.strip('\n')))
        sum1 += parse_line_partone(line.strip('\n'))
        sum2.append(parse_line_parttwo(line.strip('\n')))
    sum2.remove(0)
    sum2 = sorted(filter((0).__ne__, sum2))
    sum3 = sum2[int(len(sum2)/2)]
    return sum1, sum3

def parse_line_parttwo(line):
    opened = []
    sum = 0
    for i in range(len(line)):
        char = line[i]
        if char in OPENINGS:
            opened.append(char)
        if char in ENDINGS:
            lastopened = opened.pop()
            if OPENINGS.index(lastopened) != ENDINGS.index(char):
                print("line broken skip")
                return 0
    opened.reverse()
    for c in opened:
        e = OPENINGS.index(c)
        ec = ENDINGS[e]
        sum *= 5
        if ec == ')':
            sum += 1
        if ec == ']':
            sum += 2
        if ec == '}':
            sum += 3
        if ec == '>':
            sum += 4
    return sum

    

def parse_line_partone(line):
    opened = []
    sum = 0
    for i in range(len(line)):
        char = line[i]
        if char in OPENINGS:
            opened.append(char)
        if char in ENDINGS:
            lastopened = opened.pop()
            if OPENINGS.index(lastopened) != ENDINGS.index(char):
                print("line broken")
                if char == ')':
                    sum += 3
                if char == ']':
                    sum += 57
                if char == '}':
                    sum += 1197
                if char == '>':
                    sum += 25137
    return sum

if __name__ == '__main__':
    lines = read_input()
    # part one
    print("sum {0}".format(parse_lines(lines)))