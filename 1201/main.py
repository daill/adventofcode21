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