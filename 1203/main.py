import os


def extract_rate():
    with open(os.path.abspath('./1203/input')) as file:
        lines = file.readlines()
        ones = [0] * (len(lines[0])-1)
        zeros = [0] * (len(lines[0])-1)
                    
        for line in lines:
            for i in range(len(line)-1):
                if line[i] == '1':
                    ones[i] += 1
                else:
                    zeros[i] += 1
    print("zeros {0} \n ones {1}".format(str(zeros), str(ones)))
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
    extract_rate()
