import os

def measure():
    count = 0
    with open(os.path.abspath('./1201/depths')) as file:
        lines = file.readlines()
        prevDepth = 0
        for line in lines:
            if prevDepth < int(line) and prevDepth != 0:
                count += 1
            prevDepth = int(line)

        return count
    

if __name__ == '__main__':
    print("increased: {0} times".format(measure()))