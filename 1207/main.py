
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
    crabs = {}
    with open(os.path.abspath("./1207/input")) as file: 
        lines = file.readlines()
        for line in lines:
            for crab in line.split(','):
                if int(crab) in crabs:
                    crabs[int(crab)] += 1
                else: 
                    crabs[int(crab)] = 1
    print("crabs {0}".format(crabs))
    return crabs

# part two
def calc_fuel(diff):
    return (diff*(diff+1)/2)

def minimize(crabs):
    smallest = min(crabs.keys())
    biggest = max(crabs.keys())
    sum = -1
    newSum = -1
    while biggest >= smallest:
        tempSum1 = 0
        tempSum2 = 0
        for crab in crabs.keys():
            # part one just remove the calc_fuel function
            tempSum1 += calc_fuel(abs(smallest-crab))*crabs[crab]
            tempSum2 += calc_fuel(abs(biggest-crab))*crabs[crab]
        if tempSum2 < tempSum1:
            newSum = tempSum2
        else:
            newSum = tempSum1
        smallest += 1
        biggest -= 1
        if sum == -1 or sum > newSum:
            sum = newSum
    print("sum {0}".format(sum))

if __name__ == '__main__':
    crabs = read_input()
    minimize(crabs)