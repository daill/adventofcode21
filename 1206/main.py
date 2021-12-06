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

def simulation(fishtank):
    fishes = {}
    for i in range(9):
        if i in fishtank:
            if i != 0:
                if i-1 in fishes:
                    fishes[i-1] += fishtank[i]
                else: 
                    fishes[i-1] = fishtank[i]
            else:
                fishes[6] = fishtank[i]
                fishes[8] = fishtank[i]
    return fishes
 
def read_input():
    fishtank = {}
    with open(os.path.abspath("./1206/input")) as file: 
        lines = file.readlines()
        for line in lines:
            for fish in line.split(','):
                if int(fish) in fishtank:
                    fishtank[int(fish)] += 1
                else: 
                    fishtank[int(fish)] = 1
    return fishtank

if __name__ == '__main__':
    fishtank = read_input()
    for i in range(256):
        fishtank = simulation(fishtank)
    sum = 0
    for i in range(9):
        sum += fishtank[i]
    print("fishtank {0}".format(sum))