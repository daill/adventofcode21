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
from typing import DefaultDict
import re
from collections import Counter

def read_input():
    rules = DefaultDict()
    formula = None
    with open(os.path.abspath("./1214/input")) as file: 
        lines = file.readlines()
        for i, line in enumerate(lines):
            if '->' in line:
                splitted = re.sub('[\s+\n]', '', line).split("->")
                rules[splitted[0]] = splitted[1]
            if i == 0:
                formula = line.strip('\n')

    return rules, formula

def insertions(formular_dict, rules):
    merge_dict = DefaultDict(int)
    for k in iter(formular_dict.keys()):
        to_add = formular_dict[k]
        merge_dict[k[0] + rules[k]] += to_add
        merge_dict[rules[k] + k[1]] += to_add

    return merge_dict

if __name__ == '__main__':
    rules, formula = read_input()
    formular_dict = DefaultDict(int)
    for i in range(len(formula)):
        if i+1 < len(formula):
            keys = formula[i:(i+2)]
            formular_dict[keys] += 1
    for i in range(40):   
        formular_dict = insertions(formular_dict, rules)        
    
    cnt = DefaultDict(int)
    for f in formular_dict:
        cnt[f[1]] += formular_dict[f]
    cnt[formula[0]] += 1
    vals = list(cnt.values())
    vals.sort()
    print(vals[-1]-vals[0])
    pass