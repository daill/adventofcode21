import os
from collections import Counter

numbers = {"abcefg": "0", "cf":"1","acdeg":"2","acdfg":"3","bcdf":"4","abdfg":"5","abdefg":"6","acf":"7","abcdefg":"8","abcdfg":"9"}
# abcdf -> g
# abcdfg -> e
# a g e (cf|bd) -> 

# "abcdefg":"8"
# "abcefg": "0"
# "abdefg":"6"
# "abcdfg":"9"
# "acdeg":"2"
# "acdfg":"3"
# "abdfg":"5"


def read_input():
    firsts = list()
    seconds = list()
    with open(os.path.abspath("./1208/input")) as file: 
        lines = file.readlines()
        for line in lines:
            l = line.rstrip('\n').split(' | ')
            firsts.append(l[0].split(" "))
            seconds.append(l[1].split(" "))
    print(firsts)
    return firsts, seconds


def create_alphabet(numList):
    one = [x for x in numList if len(x) == 2][0]
    seven = [x for x in numList if len(x) == 3][0]
    four = [x for x in numList if len(x) == 4][0]
    
    a = seven.replace(one[0], '').replace(one[1], '')
    g = None
    e = None
    f = None
    b = None
    c = None
    d = None
    cf = one
    bd = four.replace(one[0], '').replace(one[1], '')
    fg = None
    dg = None
    eg = None
    
    for num in numList:
        if len(num) == 5:
            if bd[0] in num and bd[1] in num:
                fg = num.replace(a, '').replace(bd[0], '').replace(bd[1], '')
            if cf[0] in num and cf[1] in num:
                dg = num.replace(a, '').replace(cf[0], '').replace(cf[1], '')
        elif len(num) == 6:
            if bd[0] in num and bd[1] in num and cf[0] in num and cf[1]:
                g = num.replace(a, '').replace(cf[0], '').replace(cf[1], '').replace(bd[0], '').replace(bd[1], '')
        elif len(num) == 7:
            if bd[0] in num and bd[1] in num and cf[0] in num and cf[1]:
                eg = num.replace(a, '').replace(cf[0], '').replace(cf[1], '').replace(bd[0], '').replace(bd[1], '')

    if fg and dg:
        g = fg[0] if fg[0] == dg[1] or fg[0] == dg[0] else fg[1]
        f = fg.replace(g, '')
        d = dg.replace(g, '')
    if eg and dg:
        g = eg[0] if eg[0] == dg[1] or eg[0] == dg[0] else eg[1]
        e = eg.replace(g, '')
        d = dg.replace(g, '')
    if eg and fg:
        g = eg[0] if eg[0] == fg[1] or eg[0] == fg[0] else eg[1]
        e = eg.replace(g, '')
        f = fg.replace(g, '')
    if cf and fg:
        f = cf[0] if cf[0] == fg[1] or cf[0] == fg[0] else cf[1]
        c = cf.replace(f, '')
        g = fg.replace(f, '')
    if d:
        b = bd.replace(d, '')
    
    return {a: "a",b: "b",c: "c",d: "d",e: "e",f: "f",g: "g"}

def decrypt(alphabet, seconds):
    number = ""
    for num in seconds:
        seq = ""
        for i in range(len(num)):
            seq += alphabet[num[i]]
        res = ''.join(sorted(seq))
        if res in numbers.keys():
            number += numbers[res]
    print("number {0}".format(number))
    if number == '':
        return "0"
    return number

def count(numList):
    sum = 0
    for numL in numList:
        for number in numL:
            l  = len(number)
            if l == 2 or l == 3 or l == 4 or l == 7:
                sum += 1
    return sum

if __name__ == '__main__':
    firsts, seconds = read_input()
    # part one
    #print("{0}".format(count(seconds)))
    sum = 0
    for i in range(len(firsts)):
        alphabet = create_alphabet(firsts[i] + seconds[i])
        sum += int(decrypt(alphabet, seconds[i]))
    print(sum)

