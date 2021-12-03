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


def process():
    with open(os.path.abspath('./1203/input')) as file:
        lines = file.readlines()
        ones, zeros = get_bins(lines)
        print("zeros {0} \n ones {1}".format(str(zeros), str(ones)))
        part_one(ones, zeros)
        part_two(ones, zeros, lines)

def get_bins(lines):
    ones = [0] * (len(lines[0])-1)
    zeros = [0] * (len(lines[0])-1)
                
    for line in lines:
        for i in range(len(line)-1):
            if line[i] == '1':
                ones[i] += 1
            else:
                zeros[i] += 1
    print("zeros {0} ones {1}".format(str(zeros), str(ones)))
    return ones, zeros

def reduce_list(inputList, ones, zeros, i, most=True):
    leftovers = inputList
    if int(zeros[i]) > int(ones[i]):
        if most:
            leftovers = list(filter(lambda line: line[i] == '0', leftovers))
        else:
            leftovers = list(filter(lambda line: line[i] == '1', leftovers))
    else: 
        if most:
            leftovers = list(filter(lambda line: line[i] == '1', leftovers))
        else:
            leftovers = list(filter(lambda line: line[i] == '0', leftovers))
    print("leftovers {0}".format(leftovers))
    return leftovers

def part_two(ones, zeros, lines):
    # part two
    oxygen = lines
    co2scrubber = lines
    
    ones, zeros = get_bins(lines)
    for i in range(len(ones)):
        if len(oxygen) > 1:
            oxygen = reduce_list(oxygen, ones, zeros, i)
            ones, zeros = get_bins(oxygen)

    ones, zeros = get_bins(lines)
    for i in range(len(ones)):
        if len(co2scrubber) > 1:
            co2scrubber = reduce_list(co2scrubber, ones, zeros, i, False)
            ones, zeros = get_bins(co2scrubber)
        
        
    print("oxygen bin {0} co2scrubber bin {1}".format(str(oxygen[0]), str(co2scrubber[0])))
    print("oxygen dec {0} co2scrubber dec {1} product {2}".format(int(oxygen[0],2), int(co2scrubber[0], 2), (int(oxygen[0],2)*int(co2scrubber[0], 2))))

def part_one(ones, zeros):
    # part one
    gamma = ""
    epsilon = ""
    for i in range(len(ones)):
        if int(zeros[i]) > int(ones[i]):
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    print("gamma bin {0} dec {1} \n epsilon bin {2} dec {3}".format(gamma, int(gamma, 2), epsilon, int(epsilon, 2)))
    print("product {}".format(int(gamma, 2)*int(epsilon, 2)))



if __name__ == '__main__':
    process()
