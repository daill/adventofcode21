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

def measure():
    count = 0
    with open(os.path.abspath('./1201/depths')) as file:
        lines = file.readlines()
        window = []
        for line in lines:
            if len(window) < 4:
                window.append(int(line))
                print(str(window))
            else:
                print(str(window) + " " + str(sum(window)-window[3]) + "  " + str(sum(window)-window[0]))
                if (sum(window)-window[3]) < (sum(window)-window[0]):
                    count += 1
                del window[0]
                window.insert(3, int(line))
        return count


    

if __name__ == '__main__':
    print("increased: {0} times".format(measure()))