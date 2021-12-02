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
from posixpath import splitext


def move():
    with open(os.path.abspath('./1202/input')) as file:
        posH = 0
        posD = 0
        aim = 0
        lines = file.readlines()
        # split line
        for line in lines:
            splitted = line.split( )
            print(splitted)
            if splitted[0] == "forward":
                posH += int(splitted[1])
                posD += int(splitted[1]) * aim
            if splitted[0] == "down":
                aim += int(splitted[1])
            if splitted[0] == "up":
                aim -= int(splitted[1])
        print("posH {0} and posD {1} product {2}".format(posH, posD, posH*posD))


if __name__ == '__main__':
    move()