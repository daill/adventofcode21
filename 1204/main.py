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
import itertools
import re

lookupTable = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24],
    [0, 5, 10, 15, 20],
    [1, 6, 11, 16, 21],
    [2, 7, 12, 17, 22],
    [3, 8, 13, 18, 23],
    [4, 9, 14, 19, 24]
]

def read_input():
    inputNumbers = None
    cards = list()
    with open(os.path.abspath("./1204/input")) as file: 
        lines = file.readlines()
        inputNumbers = lines[0].split(',')
        cardCount = 0
        del lines[0]
        del lines[0]
        card = list()
        for line in lines:
            if line == "\n":
                # new card
                cards.append(card)
                card = list()
                cardCount += 1
                #print("skip")
                continue
            #print(line.split(" "))
            card = list(itertools.chain(card, re.findall(r'\S+', line)))
            #print(str(card))
        #print(str(cards))
        cards.append(card)
    return inputNumbers, cards

def card_match(card):
    for lookup in lookupTable:
        test = (card[lookup[0]] == 1 and card[lookup[1]] == 1 and card[lookup[2]] == 1 and card[lookup[3]] == 1 and card[lookup[4]] == 1)
        if test:
            return True
    return False

def get_value(number, card, marks):
    unmarkedSum = 0
    for i,n in enumerate(card):
        if marks[i] == 0:
            unmarkedSum += int(n)
    return unmarkedSum * int(number)

def part_one_two(inputNumbers, cards):
    marks = [list()] * len(cards)
    values = [0] *2
    firstMatchId = -1
    won = []
    for numid, number in enumerate(inputNumbers):
        for id, card in enumerate(cards):
            try:
                won.index(id)
            except ValueError:
                if len(marks[id]) == 0:
                    marks[id] = [0] * len(card)
                try:
                    cardIndex = card.index(number.strip())
                    marks[id][cardIndex] = 1
                    #print("id {0} card {1} \n number {2} index {3} \n marks {4}".format(id, card, number, cardIndex, marks[id]))
                except ValueError:
                    # do nothing
                    continue
                if numid >= 4:
                    if card_match(marks[id]):
                        print("number {0} match!! card {1} marks {2}".format(number, card, marks[id]))
                        solutionValue = get_value(number, card, marks[id])
                        values.append(solutionValue) 
                        won.append(id)
            
    return values
    #print(str(marks))


if __name__ == '__main__':
    inputNumbers, cards = read_input()
    value = part_one_two(inputNumbers, cards)
    print("values {0}".format(value))

