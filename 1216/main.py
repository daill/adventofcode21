import os
import binascii
from functools import reduce


class BinStreamEmptyError(Exception):
    pass

def read_input():
    message = 'F'
    with open(os.path.abspath("./1216/input")) as file: 
        lines = file.readlines()
        for line in lines:
            message += line.strip("\n")
    return message

def get_ver_id(bin_message):
    version = int(read_bits(bin_message,start=0, end=3), 2)
    id = int(read_bits(bin_message,start=3, end=6), 2)
    return version, id, bin_message[6:]

def get_number(bin_message):
    number = ''
    for i in range(0, len(bin_message), 5):
        fivers = bin_message[i:i+5]
        if len(fivers) == 5:
            if fivers[0] == '0':
                number += fivers[1:]
                return int(number, 2), bin_message[i+5:]
            else:
                number += fivers[1:]
        else:
            t = i+(4-(i+6)%4)
            return int(number,2), bin_message[t:]

def read_bits(bin_message, start=0, end=0):
    if len(bin_message) > 0:
        return bin_message[start:end]
    raise BinStreamEmptyError


def get_operator(bin_message, versions, op_type):
    id = read_bits(bin_message, end=1)
    bin_message = bin_message[1:]
    numbers = []
    if id == '0':
        length = int(read_bits(bin_message, end=15), 2)
        bin_message = bin_message[15:]
        sub = bin_message[:length]
        while len(sub) > 0:
            number, sub = decrypt_group(sub, versions)
            numbers.append(number)
        bin_message = bin_message[length:]
    else:
        cnt = int(read_bits(bin_message,end=11), 2)
        bin_message = bin_message[11:]
        for i in range(cnt):
            number, bin_message = decrypt_group(bin_message, versions)
            numbers.append(number)
    #0 sum
    #1 product
    #2 min
    #3 max
    #5 >
    #6 <
    #7 =

    result = 0
    if op_type == 0:
        result = sum(numbers)
    elif op_type == 1:
        result = reduce((lambda x, y: x * y), numbers)
    elif op_type == 2:
        numbers.sort()
        result = numbers[0]
    elif op_type == 3:
        numbers.sort()
        result = numbers[-1]
    elif op_type == 5:
        result = 1 if numbers[0] > numbers[1] else 0
    elif op_type == 6:
        result = 1 if numbers[0] < numbers[1] else 0
    elif op_type == 7:
        result = 1 if numbers[0] == numbers[1] else 0

    return result, bin_message


def decrypt_group(bin_message, versions):
    if len(bin_message) > 6:
        version, id, bin_message = get_ver_id(bin_message)
        versions.append(version)

        if id == 4:
            number, bin_message = get_number(bin_message)
        elif id != 4:
            number, bin_message = get_operator(bin_message, versions, id)

    return number, bin_message

if __name__ == '__main__':
    message = read_input()
    bin_message = format(int(message, 16), '04b')[4:]
    versions = list()
    print(decrypt_group(bin_message, versions))
    print(sum(versions))
    pass