import csv
import matplotlib.pyplot as plt
import numpy as np

def readCsv():
    arr = []
    with open('inclusiveOutput.csv') as csvfile:
        valueReader = csv.reader(csvfile)
        minval = -1
        for row in valueReader:
            if row[2] == '0' or row[3] == '0':
                continue

            if minval == -1:
                minval = int(row[2])
            else:
                minval = min(minval, int(row[2]))

            arr.append(row)

    fig, ax = plt.subplots(3)

    for ax_ in ax:
        ax_.set_yticks(np.arange(33))

    functocolor = {
        1 : 'green',
        2 : 'blue',
        3 : 'red'
    }

    for row in arr:
        func = int(row[0])
        id = int(row[1])
        start = int(row[2]) - minval
        width = int(row[3]) - int(row[2])
        ax[func-1].broken_barh([(start, width)],(id, 1), facecolor=functocolor[func])

    plt.show()

if __name__ == "__main__":
    readCsv()